import numpy as np
import pandas as pd


def process_ecg_file(file, filename: str):
    """
    Reads an uploaded ECG file and returns
    a validated ECG signal.
    """

    extension = filename.lower().split(".")[-1]

    if extension == "csv":

        df = pd.read_csv(file, header=None)
        ecg = df.values.flatten()

    elif extension == "txt":

        ecg = np.loadtxt(file)

    else:

        raise ValueError("Only CSV and TXT files are supported.")

    ecg = np.array(ecg, dtype=np.float32)

    if len(ecg) < 1250:
        raise ValueError(
            f"ECG contains only {len(ecg)} samples. Minimum required is 1250."
        )

    ecg = ecg[:1250]

    return ecg.tolist()