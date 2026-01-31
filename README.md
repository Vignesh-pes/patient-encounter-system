
### Why this design?
- Clear **separation of concerns**
- Business logic isolated from API routes
- Easy to test, maintain, and scale

---

## ⚙️ Tech Stack

| Layer | Technology |
|-----|-----------|
| API | FastAPI |
| ORM | SQLAlchemy |
| Database | MySQL |
| Migrations | Alembic |
| Validation | Pydantic |
| Testing | Pytest + pytest-cov |
| CI/CD | GitHub Actions |
| Code Quality | Ruff, Black, Bandit |

---

## 🚀 Features

### 👤 Patient Management
- Create a patient
- Retrieve patient by ID
- Email validation and uniqueness

### 🩺 Doctor Management
- Create a doctor
- Retrieve doctor by ID
- Enable/disable doctors using `is_active`

### 📅 Appointment Scheduling
- Schedule appointments
- Prevent overlapping appointments for the same doctor
- Reject appointments in the past
- Enforce timezone-aware datetimes
- Query appointments by date (and optional doctor)

---

## 🧠 Business Rules Enforced

- Appointments must be **in the future**
- Appointments must be **timezone-aware**
- Doctors must be **active** to accept appointments
- **No overlapping appointments** for the same doctor
- Appointment `end_time` is **derived**, not stored
- Data integrity handled at the service layer

---

## 🔗 API Endpoints

### Patients
| Method | Endpoint |
|------|---------|
| POST | `/patients` |
| GET | `/patients/{patient_id}` |

### Doctors
| Method | Endpoint |
|------|---------|
| POST | `/doctors` |
| GET | `/doctors/{doctor_id}` |

### Appointments
| Method | Endpoint |
|------|---------|
| POST | `/appointments` |
| GET | `/appointments?date=YYYY-MM-DD&doctor_id=` |

### Health Check
