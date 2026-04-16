from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storageops.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'storageops-secret-key'

db = SQLAlchemy(app)


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
    app.run(debug=True, port=5000)