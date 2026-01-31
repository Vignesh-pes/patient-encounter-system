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

