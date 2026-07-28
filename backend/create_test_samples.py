import os
import numpy as np

# Load processed dataset
X = np.load("../datasets/processed/X.npy")
y = np.load("../datasets/processed/y.npy")

# Output folder
OUTPUT_FOLDER = "sample_ecg"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

normal_count = 0
afib_count = 0

for i in range(len(y)):

    label = int(y[i])

    # Save 10 Normal samples
    if label == 0 and normal_count < 10:

        filename = os.path.join(
            OUTPUT_FOLDER,
            f"normal_{normal_count+1}.txt"
        )

        np.savetxt(filename, X[i].flatten())

        normal_count += 1

    # Save 10 AFIB samples
    elif label == 1 and afib_count < 10:

        filename = os.path.join(
            OUTPUT_FOLDER,
            f"afib_{afib_count+1}.txt"
        )

        np.savetxt(filename, X[i].flatten())

        afib_count += 1

    if normal_count == 10 and afib_count == 10:
        break

print("Created 20 ECG test files successfully.")