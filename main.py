from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud
from database import SessionLocal, engine
from typing import List

app = FastAPI(
    title="Angelo Indre - RESTORE-Skills Application",
)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root
@app.get("/")
def read_root():
    return {"message": "Welcome to RESTORE-Skills Application Take Home Assessment - Angelo Indre"}

### THERAPIST ROUTES
# Create therapist
@app.post("/therapists/", response_model=schemas.Therapist)
def create_therapist_route(therapist: schemas.TherapistCreate, db: Session = Depends(get_db)):
    return crud.create_therapist(db, therapist)
    
# Get a therapist  
@app.get("/therapists/{therapist_id}", response_model=schemas.Therapist)
def get_therapist_route(therapist_id: int, db: Session = Depends(get_db)):   
    therapist = crud.get_therapist(db, therapist_id)
    if not therapist:
        raise HTTPException(status_code=404, detail="Therapist not found")
    return therapist

# Get all therapists
@app.get("/therapists/", response_model=List[schemas.Therapist])
def list_therapists(db: Session = Depends(get_db)):
    return crud.get_therapists(db)

# Remove a therapist
@app.delete("/therapists/{therapist_id}", response_model=schemas.Therapist)
def delete_patient_route(therapist_id: int, db: Session = Depends(get_db)):
    therapist = crud.delete_therapist(db, therapist_id)
    if not therapist:
        raise HTTPException(status_code=404, detail="Therapist not found")
    return therapist

### PATIENT ROUTES
# Create a patient
@app.post("/patients/", response_model=schemas.Patient)
def create_patient_route(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

# Get a patient
@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def get_patient_route(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Get all patients
@app.get("/patients/", response_model=List[schemas.Patient])
def get_patients_route(db: Session = Depends(get_db)):
    return crud.get_patients(db)

# Remove a patient
@app.delete("/patients/{patient_id}", response_model=schemas.Patient)
def delete_patient_route(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

### NUKE TABLES
@app.delete("/clear/")
def clear_tables(db: Session = Depends(get_db)):
    crud.clear(db)
    return {"detail": "All tables cleared"}