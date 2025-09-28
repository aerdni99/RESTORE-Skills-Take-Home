"""
    schemas.py
"""

from pydantic import BaseModel
from typing import List, Optional

class PatientBase(BaseModel):
    name: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    therapist_id: Optional[int] = None

    class Config:
        orm_mode = True

class TherapistBase(BaseModel):
    name: str

class TherapistCreate(TherapistBase):
    pass

class Therapist(TherapistBase):
    id: int
    patients: List[Patient] = []

    class Config:
        orm_mode = True
