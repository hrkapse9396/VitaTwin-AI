from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from .database import Base


class Patient(Base):

    __tablename__ = "patients"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String
    )


    age = Column(
        Integer
    )


    gender = Column(
        String
    )


    created_date = Column(
        DateTime,
        default=datetime.utcnow
    )



class ECGPrediction(Base):

    __tablename__ = "ecg_predictions"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    patient_id = Column(
        Integer
    )


    prediction = Column(
        String
    )


    confidence = Column(
        Float
    )


    risk_score = Column(
        Float
    )


    risk_level = Column(
        String
    )


    timestamp = Column(
        DateTime,
        default=datetime.utcnow
    )