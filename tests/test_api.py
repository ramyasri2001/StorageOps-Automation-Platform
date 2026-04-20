import pytest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.app import app, db
from api.models import Volume


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()


def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'


def test_create_volume(client):
    response = client.post('/api/volumes',
        json={
            'name': 'test-vol',
            'total_capacity_gb': 500
        })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['volume']['name'] == 'test-vol'
    assert data['volume']['used_capacity_gb'] == 0


def test_critical_detection(client):
    with app.app_context():
        volume = Volume(
            name='critical-vol',
            total_capacity_gb=100,
            used_capacity_gb=95
        )
        assert volume.utilization_pct == 95.0
        assert volume.is_critical == True


def test_not_critical_below_90(client):
    with app.app_context():
        volume = Volume(
            name='healthy-vol',
            total_capacity_gb=100,
            used_capacity_gb=85
        )
        assert volume.is_critical == False


def test_duplicate_volume_rejected(client):
    client.post('/api/volumes',
        json={'name': 'vol-001', 'total_capacity_gb': 500})
    response = client.post('/api/volumes',
        json={'name': 'vol-001', 'total_capacity_gb': 500})
    assert response.status_code == 409