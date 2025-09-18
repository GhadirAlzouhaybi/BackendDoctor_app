from pydantic import BaseModel
from sqlalchemy import Column, Integer, String 
from database import Base


class Doctor(BaseModel):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    fullName = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    specialty = Column(String)
    workplace = Column(String)
    experience = Column(String)
    qualifications = Column(String)
    availability = Column(String)
    linkedin = Column(String)