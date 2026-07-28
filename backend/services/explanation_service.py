import numpy as np

from model.model_loader import model


def generate_explanation(ecg_data):

    ecg_array = np.array(ecg_data)

    original_length = len(ecg_array)

    ecg_input = ecg_array.reshape(
        1,
        1250,
        1
    )

    prediction = model.predict(ecg_input)

    probability = float(prediction[0][0])

    if probability >= 0.5:
        result = "AFIB"
    else:
        result = "NORMAL"

    signal_variation = np.std(ecg_array)

    important_regions = []

    window_size = 100

    for i in range(0, original_length, window_size):

        segment = ecg_array[i:i + window_size]

        if len(segment) > 0:

            variation = np.std(segment)

            if variation > signal_variation:

                important_regions.append(i)

    if len(important_regions) == 0:

        important_regions = [
            0,
            250,
            500
        ]

    # -----------------------------
    # Dynamic AI Explanation
    # -----------------------------

    if result == "NORMAL":

        summary = "Normal sinus rhythm detected."

        finding = "No significant cardiac abnormality was identified in the ECG waveform."

        recommendation = "Continue routine cardiac monitoring and maintain a healthy lifestyle."

    else:

        summary = "Possible Atrial Fibrillation detected."

        finding = "The ECG waveform shows irregular rhythm patterns consistent with atrial fibrillation."

        recommendation = "Consult a cardiologist for further clinical evaluation."

    return {

        "prediction": result,

        "confidence": round(probability * 100, 2),

        "summary": summary,

        "finding": finding,

        "recommendation": recommendation,

        "important_regions": important_regions[:5]

    }