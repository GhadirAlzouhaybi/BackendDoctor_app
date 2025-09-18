from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine, Base
import Model 

app = FastAPI()

Base.metadata.create_all(bind=engine)

# @app.get("/")
# def read_root():
#     return {"message": "Hello world"}

# @app.get("/ping")
# def ping():
#     return {"status": "ok"}
def get_db():
 db = SessionLocal()
 try:
    yield db
finally:
    db.close()

class UserSchema(BaseModel):
    email: Str
    password: Str

class DoctorSchema(BaseModel):
   fullName: Str
    email: Str
    password: Str
    specialty: Str
    workplace: Str
    experience: Str
    qualifications: Str
    availability: Str
    linkedin: Str 


@app.post("/signup/user")
def signup_user(user: UserSchema, db: Session = Depends(get_db)):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User signed up successful", "id": db_user.id}


@app.post("/signup/doctor")
def signup_doctor(doctor: DoctorSchema, db: Session = Depends(get_db)):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return {"message": "Doctor signed up successful", "id": db_doctor.id}

@app.post("/signin")
def signin(user: User):
    for u in users:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "User SignIn successful"}
    for d in doctors:
        if d["email"] == user.email and d["password"] == user.password:
            return {"message": "Doctor SignIn successful"}
    return {"message": "Invalid credentials"}