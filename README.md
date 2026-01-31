# 🏥 Medical Encounter Management System

A **production-grade FastAPI backend** for managing patients, doctors, and medical appointments with strict validation, conflict detection, and high test coverage.

This project follows **real-world backend engineering standards**: clean architecture, service layer separation, validation-first design, and CI/CD readiness.

---

## 🚀 Features

### 👤 Patient Management
- Create patients with validated data
- Retrieve patients by ID
- Prevent duplicate emails

### 👨‍⚕️ Doctor Management
- Create doctors
- Retrieve doctors by ID
- Support active/inactive doctors

### 📅 Appointment Scheduling
- Create appointments with:
  - Future time validation
  - Timezone awareness
  - Doctor availability checks
  - Conflict detection
- List appointments by date and doctor

### ✅ Engineering Quality
- Clean service-based architecture
- Pydantic schema validation
- SQLAlchemy ORM
- 98%+ pytest coverage
- CI/CD ready with GitHub Actions

---

## 🗂 Project Structure
patient-encounter-system/
│
├── src/
│ ├── main.py # FastAPI application entrypoint
│ ├── database.py # DB connection & session
│ │
│ ├── models/ # SQLAlchemy models
│ │ ├── patient.py
│ │ ├── doctor.py
│ │ └── appointment.py
│ │
│ ├── schemas/ # Pydantic schemas
│ │ ├── patient.py
│ │ ├── doctor.py
│ │ └── appointment.py
│ │
│ └── services/ # Business logic layer
│ ├── patient_service.py
│ ├── doctor_service.py
│ └── appointment_service.py
│
├── tests/ # Pytest test suite
│ ├── conftest.py
│ ├── test_patient_service.py
│ ├── test_doctor_service.py
│ ├── test_appointment_service.py
│ └── test_appointment_model.py
│
├── requirements.txt
├── pyproject.toml
└── README.md


---

## 🧪 Test Coverage

- **Overall Coverage:** **98%**
- Business logic fully tested
- Edge cases covered:
  - Duplicate patients
  - Invalid doctors
  - Past appointments
  - Conflicting appointments

Run tests:

```bash
pytest --cov=src

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/<your-username>/patient-encounter-system.git
cd patient-encounter-system

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create a .env file:

DATABASE_URL=mysql+pymysql://username:password@host:3306/database_name


Defaults to MySQL but can be changed easily.

▶️ Running the Application
uvicorn main:app --reload --app-dir src


Server starts at:

http://127.0.0.1:8000

📘 API Documentation

FastAPI auto-generated docs:

Swagger UI:
👉 http://127.0.0.1:8000/docs

OpenAPI JSON:
👉 http://127.0.0.1:8000/openapi.json

🔌 API Endpoints
Patients
Method	Endpoint	Description
POST	/patients	Create patient
GET	/patients/{id}	Get patient
Doctors
Method	Endpoint	Description
POST	/doctors	Create doctor
GET	/doctors/{id}	Get doctor
Appointments
Method	Endpoint	Description
POST	/appointments	Create appointment
GET	/appointments	List appointments
🛡 Validation Rules
Patient

Email must be valid

Name length ≥ 2

Email must be unique

Doctor

Must exist

Must be active

Appointment

Must be in the future

Must be timezone-aware

No overlapping appointments per doctor

🔁 CI/CD (GitHub Actions)

Pipeline includes:

Dependency installation

Linting (Black, Ruff)

Security scan (Bandit)

Pytest with coverage

✔ Fails build if tests fail
✔ Ensures production safety

🧠 Design Principles

Separation of concerns

Service-driven logic

Explicit error handling

Defensive validation

Test-first mindset

🏁 Health Check
GET /


Response:

{
  "status": "ok"
}

📌 Status

✔ Production-ready
✔ Fully tested
✔ CI/CD enabled
✔ Clean architecture

👨‍💻 Author

Vignesh J
Backend Engineer | FastAPI | SQLAlchemy | Testing & CI/CD

⭐ Final Note

This project is intentionally built to industry standards and can be extended to:

Auth (JWT)

Role-based access

Notifications

Docker & Kubernetes

Cloud deployment




