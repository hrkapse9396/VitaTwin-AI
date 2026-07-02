import numpy as np

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from model.model_loader import model



X_PATH = "../datasets/processed/X.npy"

Y_PATH = "../datasets/processed/y.npy"





def evaluate_model():


    X_test = np.load(X_PATH)

    y_test = np.load(Y_PATH)



    print(
        "Original X shape:",
        X_test.shape
    )


    print(
        "Original Y shape:",
        y_test.shape
    )



    # Fix ECG input shape for CNN model

    if len(X_test.shape) == 2:


        X_test = X_test.reshape(

            X_test.shape[0],

            X_test.shape[1],

            1

        )



    print(
        "Model input shape:",
        X_test.shape
    )



    predictions = model.predict(
        X_test
    )



    predictions = (

        predictions >= 0.5

    ).astype(int).flatten()



    y_test = y_test.flatten()



    accuracy = accuracy_score(
        y_test,
        predictions
    )


    precision = precision_score(
        y_test,
        predictions
    )


    recall = recall_score(
        y_test,
        predictions
    )


    f1 = f1_score(
        y_test,
        predictions
    )



    cm = confusion_matrix(
        y_test,
        predictions
    )



    return {


        "accuracy": round(
            accuracy * 100,
            2
        ),


        "precision": round(
            precision * 100,
            2
        ),


        "recall": round(
            recall * 100,
            2
        ),


        "f1_score": round(
            f1 * 100,
            2
        ),



        "confusion_matrix": {


            "true_negative": int(
                cm[0][0]
            ),


            "false_positive": int(
                cm[0][1]
            ),


            "false_negative": int(
                cm[1][0]
            ),


            "true_positive": int(
                cm[1][1]
            )


        }

    }