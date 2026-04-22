from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storageops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'storageops-secret-key'

db = SQLAlchemy(app)
metrics = PrometheusMetrics(app)

# Custom metrics
metrics.info('storageops_info', 'StorageOps Application Info', version='1.0.0')


@app.route('/api/health')
def health():
    return {
        'status': 'healthy',
        'service': 'StorageOps Automation Platform',
        'version': '1.0.0'
    }


from api import routes


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database ready!")
    app.run(debug=True, port=8080)