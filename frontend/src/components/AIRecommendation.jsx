function AIRecommendation({recommendation}) {

    if (!recommendation) {
        return (
            <div className="card recommendation-card">
                <h2>🧠 AI Health Recommendation</h2>
                <p>Loading patient-specific recommendations...</p>
            </div>
        );
    }

    if (recommendation.message && !recommendation.recommendations) {
        return (
            <div className="card recommendation-card">
                <h2>🧠 AI Health Recommendation</h2>
                <p>{recommendation.message}</p>
            </div>
        );
    }

    return (
        <div className="card recommendation-card">
            <h2>🧠 AI Health Recommendation</h2>

            <p>
                <strong>Monitoring Priority:</strong>{" "}
                {recommendation.monitoring_priority}
            </p>

            <p>{recommendation.summary}</p>

            <ul>
                {recommendation.recommendations?.map((item, index) => (
                    <li key={`${item.type}-${index}`}>
                        <strong>{item.title}:</strong> {item.message}
                    </li>
                ))}
            </ul>

            <small>
                {recommendation.disclaimer}
            </small>
        </div>
    );
}

export default AIRecommendation;