import "./HealthIntelligence.css";

function HealthIntelligence({ intelligence }) {

    if (!intelligence) {

        return null;

    }

    return (

        <div className="card">

            <div className="card-header">
                <h2>Predictive Health Intelligence</h2>
            </div>

            <div className="health-grid">

                <div>
                    <strong>Future Risk</strong>
                    <p>{intelligence.future_risk}</p>
                </div>

                <div>
                    <strong>Risk Score</strong>
                    <p>{intelligence.future_risk_score}%</p>
                </div>

                <div>
                    <strong>Cardiac Stability</strong>
                    <p>{intelligence.cardiac_stability}</p>
                </div>

                <div>
                    <strong>Disease Progression</strong>
                    <p>{intelligence.disease_progression}</p>
                </div>

                <div>
                    <strong>Clinical Priority</strong>
                    <p>{intelligence.clinical_priority}</p>
                </div>

                <div>
                    <strong>Recommended Follow-up</strong>
                    <p>{intelligence.recommended_follow_up}</p>
                </div>

            </div>

        </div>

    );

}

export default HealthIntelligence;