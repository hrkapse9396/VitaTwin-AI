from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from database.database import SessionLocal
from database.models import Patient, ECGPrediction

from services.health_intelligence_service import generate_health_intelligence
from services.patient_twin_service import generate_patient_twin
from services.recommendation_service import generate_recommendations

import os


def generate_pdf_report(patient_id: int):

    db = SessionLocal()

    try:

        patient = (
            db.query(Patient)
            .filter(Patient.id == patient_id)
            .first()
        )

        if patient is None:
            return None

        history = (
            db.query(ECGPrediction)
            .filter(ECGPrediction.patient_id == patient_id)
            .order_by(ECGPrediction.timestamp.desc())
            .all()
        )

        if len(history) == 0:
            return None

        latest = history[0]

        intelligence = generate_health_intelligence(patient_id)
        twin = generate_patient_twin(patient_id)
        recommendations = generate_recommendations(patient_id)

        os.makedirs("reports", exist_ok=True)

        filename = f"reports/patient_{patient_id}_report.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = []

        # =====================================
        # Title
        # =====================================

        elements.append(
            Paragraph(
                "VitaTwin AI Health Report",
                styles["Title"]
            )
        )

        elements.append(Spacer(1, 20))

        # =====================================
        # Patient Information
        # =====================================

        elements.append(
            Paragraph(
                "<b>Patient Information</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(f"Name : {patient.name}", styles["Normal"])
        )
        elements.append(
            Paragraph(f"Age : {patient.age}", styles["Normal"])
        )
        elements.append(
            Paragraph(f"Gender : {patient.gender}", styles["Normal"])
        )

        elements.append(Spacer(1, 15))

        # =====================================
        # Latest Prediction
        # =====================================

        elements.append(
            Paragraph(
                "<b>Latest ECG Prediction</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Prediction : {latest.prediction}",
                styles["Normal"]
            )
        )
        elements.append(
            Paragraph(
                f"Confidence : {latest.confidence:.2f} %",
                styles["Normal"]
            )
        )
        elements.append(
            Paragraph(
                f"Risk Score : {latest.risk_score:.2f}",
                styles["Normal"]
            )
        )
        elements.append(
            Paragraph(
                f"Risk Level : {latest.risk_level}",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        # =====================================
        # Predictive Health Intelligence
        # =====================================

        elements.append(
            Paragraph(
                "<b>Predictive Health Intelligence</b>",
                styles["Heading2"]
            )
        )

        for key, value in intelligence.items():
            elements.append(
                Paragraph(
                    f"{key.replace('_',' ').title()} : {value}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 15))

        # =====================================
        # Patient Twin
        # =====================================

        elements.append(
            Paragraph(
                "<b>VitaTwin Patient Profile</b>",
                styles["Heading2"]
            )
        )

        for key, value in twin.items():
            elements.append(
                Paragraph(
                    f"{key.replace('_',' ').title()} : {value}",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 15))

        # =====================================
        # AI Health Recommendations
        # =====================================

        elements.append(
            Paragraph(
                "<b>AI Health Recommendations</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Monitoring Priority : {recommendations.get('monitoring_priority', 'LOW')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                recommendations.get("summary", "No recommendation summary available."),
                styles["Normal"]
            )
        )

        for item in recommendations.get("recommendations", []):
            elements.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        elements.append(
            Paragraph(
                f"Suggested Follow-up : {recommendations.get('recommended_follow_up', 'Routine monitoring')}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                "These recommendations are generated from the patient's stored ECG history and are intended to support monitoring. They do not replace professional medical diagnosis or treatment.",
                styles["Normal"]
            )
        )

        elements.append(Spacer(1, 15))

        # =====================================
        # Prediction History
        # =====================================

        elements.append(
            Paragraph(
                "<b>Prediction History</b>",
                styles["Heading2"]
            )
        )

        for item in history:
            elements.append(
                Paragraph(
                    f"{item.timestamp.strftime('%d-%m-%Y %H:%M')} | "
                    f"{item.prediction} | "
                    f"{item.confidence:.2f}%",
                    styles["Normal"]
                )
            )

        elements.append(Spacer(1, 20))

        # =====================================
        # Clinical Summary
        # =====================================

        elements.append(
            Paragraph(
                "<b>AI Clinical Summary</b>",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                "This report was generated using VitaTwin AI. The prediction, health intelligence, and recommendations are intended to assist clinicians and support patient monitoring. They should not replace professional medical diagnosis or treatment.",
                styles["Normal"]
            )
        )

        doc.build(elements)

        return filename

    finally:
        db.close()
