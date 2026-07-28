import { useState } from "react";
import API from "../services/api";

function ECGUpload({ patientId, onUploadSuccess }) {

    const [selectedFile, setSelectedFile] = useState(null);
    const [uploading, setUploading] = useState(false);

    const handleFileChange = (event) => {

        const file = event.target.files[0];

        if (file) {
            setSelectedFile(file);
        }

    };
    const handleUpload = async () => {

    if (!selectedFile) {

        alert("Please select an ECG file.");

        return;

    }

    const formData = new FormData();

    formData.append("patient_id", patientId);

    formData.append("file", selectedFile);

    try {

        const response = await API.post(

            "/predict/upload",

            formData,

            {

                headers: {

                    "Content-Type": "multipart/form-data"

                }

            }

        );

        alert("Prediction Completed Successfully!");

        console.log(response.data);

        if (onUploadSuccess) {

            onUploadSuccess();

        }

    }

    catch(error){

        console.log(error);

        alert("Upload Failed");

    }

};

    

    return (

        <div className="card">

            <div className="card-header">

                <h2>ECG Upload</h2>

            </div>

            <div className="upload-container">

                <input
                    type="file"
                    accept=".csv,.txt"
                    onChange={handleFileChange}
                />

                <button
                    onClick={handleUpload}
                    disabled={uploading}
                >

                    {uploading ? "Uploading..." : "Upload ECG"}

                </button>

            </div>

        </div>

    );

}

export default ECGUpload;