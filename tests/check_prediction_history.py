import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Add backend folder to Python path
sys.path.append(
    os.path.abspath("backend")
)


from database.models import ECGPrediction


DATABASE_URL = "sqlite:///database/vitatwin.db"


engine = create_engine(DATABASE_URL)


Session = sessionmaker(bind=engine)


db = Session()


records = db.query(ECGPrediction).all()


print("Prediction History:")


for r in records:

    print(
        "ID:", r.id,
        "Patient:", r.patient_id,
        "Prediction:", r.prediction,
        "Confidence:", r.confidence,
        "Risk:", r.risk_level
    )


db.close()