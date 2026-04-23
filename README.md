# StorageOps Automation Platform

A production-grade storage operations automation platform built with Python, Flask, and SQLAlchemy — inspired by enterprise storage engineering workflows.

---

## 🎯 What Problem Does This Solve?

Enterprise storage systems have thousands of volumes storing critical data. Without automation:
- Engineers manually monitor hundreds of servers
- Nobody notices when storage fills up until it crashes
- Alerts are slow and require human intervention
- Configuration takes days instead of minutes

StorageOps solves this by automating monitoring, alerting, and remediation.

---

## 🏗️ Architecture

REST API (Flask)     →    SQLite Database
↓                         ↓
Storage Simulator    →    Auto Alert Detection
↓                         ↓
pytest Tests         →    GitHub Actions CI/CD

---

## 🔧 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core automation language |
| Flask | REST API framework |
| SQLAlchemy | Database ORM |
| SQLite | Data persistence |
| pytest | Automated testing |
| Ansible | Configuration management |
| Docker | Containerization |
| Docker Compose | Multi-service orchestration |
| Prometheus | Metrics collection |
| Grafana | Metrics visualization |
| n8n | Workflow automation |
| GitHub Actions | CI/CD pipeline |
| Git/GitHub | Version control |

---

## 🚀 How to Run

**Step 1 — Clone the repository:**
```bash
git clone https://github.com/ramyasri2001/StorageOps-Automation-Platform.git
cd StorageOps-Automation-Platform
```

**Step 2 — Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Step 3 — Install dependencies:**
```bash
pip install -r requirements.txt
```

**Step 4 — Start the API server:**
```bash
FLASK_APP=api.app FLASK_DEBUG=1 flask run --port 8080
```

**Step 5 — Run the storage simulator:**
```bash
python3 simulator/storage.py
```

**Step 6 — Run automated tests:**
```bash
python3 -m pytest tests/ -v
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /api/health | Health check |
| GET | /api/volumes | Get all volumes |
| POST | /api/volumes | Create new volume |
| GET | /api/volumes/{id} | Get specific volume |
| PUT | /api/volumes/{id} | Update volume |
| DELETE | /api/volumes/{id} | Delete volume |
| GET | /api/dashboard | System summary |

---

## 🚨 Auto Alert Detection

The system automatically detects critical volumes:

```json
{
  "name": "vol-001",
  "total_capacity_gb": 1000,
  "used_capacity_gb": 950,
  "utilization_pct": 95.0,
  "is_critical": true
}
```

When `utilization_pct > 90%` → volume is flagged as critical automatically.

---

## 🧪 Test Results

tests/test_api.py::test_health_check          PASSED
tests/test_api.py::test_create_volume         PASSED
tests/test_api.py::test_critical_detection    PASSED
tests/test_api.py::test_not_critical_below_90 PASSED
tests/test_api.py::test_duplicate_volume_rejected PASSED
5 passed in 0.17s

---

## 📅 Roadmap

- [x] Week 1 — Python REST API + Storage Simulator + pytest
- [x] Week 2 — Ansible playbooks + n8n workflows
- [x] Week 3 — Docker containerization + Grafana dashboard
- [x] Week 4 — GitHub Actions CI/CD pipeline

---

## 👩‍💻 Author

**Ramyasri Kanugula**
MS Computer Science + MBA
[LinkedIn](https://linkedin.com/in/ramyasri-kanugula-763012210) | [GitHub](https://github.com/ramyasri2001)
