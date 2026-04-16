from flask import jsonify, request
from api.app import app, db
from api.models import Volume


@app.route('/api/volumes', methods=['GET'])
def get_volumes():
    volumes = Volume.query.all()
    return jsonify({
        'volumes': [v.to_dict() for v in volumes],
        'total': len(volumes),
        'critical': sum(1 for v in volumes if v.is_critical)
    })


@app.route('/api/volumes', methods=['POST'])
def create_volume():
    data = request.get_json()
    if not data or 'name' not in data or 'total_capacity_gb' not in data:
        return jsonify({'error': 'name and total_capacity_gb are required'}), 400
    existing = Volume.query.filter_by(name=data['name']).first()
    if existing:
        return jsonify({'error': f"Volume {data['name']} already exists"}), 409
    volume = Volume(
        name=data['name'],
        total_capacity_gb=data['total_capacity_gb'],
        used_capacity_gb=data.get('used_capacity_gb', 0),
        location=data.get('location', 'datacenter-1')
    )
    db.session.add(volume)
    db.session.commit()
    return jsonify({
        'message': f"Volume {volume.name} created successfully",
        'volume': volume.to_dict()
    }), 201


@app.route('/api/volumes/<int:volume_id>', methods=['GET'])
def get_volume(volume_id):
    volume = Volume.query.get_or_404(volume_id)
    return jsonify(volume.to_dict())


@app.route('/api/volumes/<int:volume_id>', methods=['PUT'])
def update_volume(volume_id):
    volume = Volume.query.get_or_404(volume_id)
    data = request.get_json()
    if 'used_capacity_gb' in data:
        volume.used_capacity_gb = data['used_capacity_gb']
    if 'status' in data:
        volume.status = data['status']
    if 'total_capacity_gb' in data:
        volume.total_capacity_gb = data['total_capacity_gb']
    db.session.commit()
    return jsonify({
        'message': f"Volume {volume.name} updated",
        'volume': volume.to_dict()
    })


@app.route('/api/volumes/<int:volume_id>', methods=['DELETE'])
def delete_volume(volume_id):
    volume = Volume.query.get_or_404(volume_id)
    db.session.delete(volume)
    db.session.commit()
    return jsonify({'message': f"Volume {volume.name} deleted"})


@app.route('/api/dashboard', methods=['GET'])
def dashboard():
    volumes = Volume.query.all()
    return jsonify({
        'summary': {
            'total_volumes': len(volumes),
            'healthy': sum(1 for v in volumes if v.status == 'healthy'),
            'critical': sum(1 for v in volumes if v.is_critical)
        },
        'volumes': [v.to_dict() for v in volumes]
    })