"""

"""

from sqlalchemy.orm import Session
import models, schemas

################################################################################################

# Therapist Queries
"""
    create_therapist takes a therapist object (defined in schemas.py) and adds it to the table.
    get_therapist searches for a particular therapist by ID.
    get_therapists returns up to 10 therapists at a time.

    delete_therapist searches for a particular therapist by ID and removes it from the table, 
    orphaning the therapist's patients along the way.
"""
def create_therapist(db: Session, therapist: schemas.TherapistCreate):
    db_therapist = models.Therapist(name=therapist.name)
    db.add(db_therapist)
    db.commit()
    db.refresh(db_therapist)
    return db_therapist

def get_therapist(db: Session, therapist_id: int):
    return db.query(models.Therapist).filter(models.Therapist.id == therapist_id).first()

def get_therapists(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Therapist).offset(skip).limit(limit).all()

def delete_therapist(db: Session, therapist_id: int):
    therapist = db.query(models.Therapist).filter(models.Therapist.id == therapist_id).first()
    if therapist:
        for patient in therapist.patients:
            patient.therapist_id = None
        db.commit()

        db.delete(therapist)
        db.commit()
    return therapist

############################################################################################

# Patient Queries
"""
    Similar to Therapist Queries aside from assign_patient_to_therapist:
    Search for a patient, set their assigned therapist_id.
"""
def create_patient(db: Session, patient: schemas.PatientCreate, therapist_id: int = None):
    db_patient = models.Patient(name=patient.name, therapist_id=therapist_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def assign_patient_to_therapist(db: Session, patient_id: int, therapist_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        patient.therapist_id = therapist_id
        db.commit()
        db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return patient

############################################################################################

# Clear the tables
def clear(db: Session):
    db.query(models.Patient).delete()
    db.query(models.Therapist).delete()
    db.commit()