from datetime import datetime
from api.app import db


class Volume(db.Model):
    __tablename__ = 'volumes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    total_capacity_gb = db.Column(db.Integer, nullable=False)
    used_capacity_gb = db.Column(db.Integer, default=0)
    status = db.Column(db.String(50), default='healthy')
    location = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def utilization_pct(self):
        if self.total_capacity_gb == 0:
            return 0
        return round((self.used_capacity_gb / self.total_capacity_gb) * 100, 2)

    @property
    def is_critical(self):
        return self.utilization_pct > 90

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'total_capacity_gb': self.total_capacity_gb,
            'used_capacity_gb': self.used_capacity_gb,
            'utilization_pct': self.utilization_pct,
            'status': self.status,
            'location': self.location,
            'is_critical': self.is_critical,
            'created_at': self.created_at.isoformat()
        }