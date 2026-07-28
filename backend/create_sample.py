import numpy as np

X = np.load("../datasets/processed/X.npy")

sample = X[0].flatten()

with open("sample_ecg.txt", "w") as f:
    for value in sample:
        f.write(f"{value}\n")

print("Sample ECG created successfully.")
print("Length:", len(sample))