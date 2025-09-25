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