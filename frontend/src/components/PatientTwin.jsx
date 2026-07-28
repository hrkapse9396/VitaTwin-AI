import "./PatientTwin.css";

function PatientTwin({ twin }) {

    if (!twin) {

        return null;

    }

    return (

        <div className="card">

            <div className="card-header">

                <h2>VitaTwin Patient Profile</h2>

            </div>

            <div className="twin-grid">

                <div>
                    <strong>Name</strong>
                    <p>{twin.patient_name}</p>
                </div>

                <div>
                    <strong>Age</strong>
                    <p>{twin.patient_age}</p>
                </div>

                <div>
                    <strong>Gender</strong>
                    <p>{twin.patient_gender}</p>
                </div>

                <div>
                    <strong>Health Score</strong>
                    <p>{twin.overall_health_score}</p>
                </div>

                <div>
                    <strong>Health Status</strong>
                    <p>{twin.health_status}</p>
                </div>

                <div>
                    <strong>Average Risk</strong>
                    <p>{twin.average_risk_score}%</p>
                </div>

                <div>
                    <strong>Highest Risk</strong>
                    <p>{twin.highest_risk}</p>
                </div>

                <div>
                    <strong>Total Predictions</strong>
                    <p>{twin.total_predictions}</p>
                </div>

                <div>
                    <strong>Latest Prediction</strong>
                    <p>{twin.latest_prediction}</p>
                </div>

            </div>

        </div>

    );

}

export default PatientTwin;