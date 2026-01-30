from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import date

from database import get_db
from schemas.patient import PatientCreate, PatientRead
from schemas.doctor import DoctorCreate, DoctorRead
from schemas.appointment import AppointmentCreate, AppointmentRead
from services.patient_service import create_patient, get_patient
from services.doctor_service import create_doctor, get_doctor
from services.appointment_service import create_appointment
from models.appointment import Appointment

app = FastAPI(
    title="Medical Encounter Management System",
    version="1.0.0",
)

# -------------------------
# PATIENT APIs
# -------------------------


@app.post("/patients", response_model=PatientRead, status_code=201)
def create_patient_api(
    data: PatientCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_patient(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/patients/{patient_id}", response_model=PatientRead)
def get_patient_api(
    patient_id: int,
    db: Session = Depends(get_db),
):
    try:
        return get_patient(db, patient_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# -------------------------
# DOCTOR APIs
# -------------------------


@app.post("/doctors", response_model=DoctorRead, status_code=201)
def create_doctor_api(
    data: DoctorCreate,
    db: Session = Depends(get_db),
):
    return create_doctor(db, data)


@app.get("/doctors/{doctor_id}", response_model=DoctorRead)
def get_doctor_api(
    doctor_id: int,
    db: Session = Depends(get_db),
):
    try:
        return get_doctor(db, doctor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# -------------------------
# APPOINTMENT APIs
# -------------------------


@app.post("/appointments", response_model=AppointmentRead, status_code=201)
def create_appointment_api(
    data: AppointmentCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_appointment(db, data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.get("/appointments", response_model=list[AppointmentRead])
def list_appointments(
    date: date,
    doctor_id: int | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Appointment)

    start = f"{date} 00:00:00"
    end = f"{date} 23:59:59"

    query = query.filter(
        Appointment.start_time >= start,
        Appointment.start_time <= end,
    )

    if doctor_id:
        query = query.filter(Appointment.doctor_id == doctor_id)

    return query.all()


@app.get("/")
def health_check():
    return {"status": "ok"}
