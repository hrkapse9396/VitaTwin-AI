function AIRecommendation({ recommendation }) {

    if (!recommendation) {
        return (
            <div className="card recommendation-card">
                <h2>🧠 AI Health Recommendation</h2>
                <p>Loading patient-specific recommendations...</p>
            </div>
        );
    }

    return (
        <div className="card recommendation-card">

            <h2>🧠 AI Health Recommendation</h2>

            <p>
                <strong>Monitoring Priority:</strong>{" "}
                {recommendation.monitoring_priority || "LOW"}
            </p>

            {recommendation.summary && (
                <p>{recommendation.summary}</p>
            )}

            <ul>
                {(recommendation.recommendations || []).map(
                    (item, index) => (
                        <li key={index}>{item}</li>
                    )
                )}
            </ul>

            {recommendation.recommended_follow_up && (
                <p>
                    <strong>Suggested Follow-up:</strong>{" "}
                    {recommendation.recommended_follow_up}
                </p>
            )}

            <p className="recommendation-disclaimer">
                These recommendations are generated from the patient's stored
                ECG history and are intended to support monitoring. They do not
                replace professional medical diagnosis or treatment.
            </p>

        </div>
    );
}

export default AIRecommendation;
