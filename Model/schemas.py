from pydantic import BaseModel

class UserSchema(BaseModel):
    email: str
    password: str

class DoctorSchema(BaseModel):
    fullName: str
    email: str
    password: str
    specialty: str
    workplace: str
    experience: str
    qualifications: str
    availability: str
    linkedin: str
