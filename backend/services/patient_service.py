from database.models import Patient
from database.database import SessionLocal


def create_patient(patient_data):

    db = SessionLocal()


    new_patient = Patient(

        name=patient_data.name,

        age=patient_data.age,

        gender=patient_data.gender

    )


    db.add(new_patient)

    db.commit()

    db.refresh(new_patient)


    db.close()


    return new_patient