function AIExplanation({ explanation }) {

    return (

        <div className="card">

            <h2>AI Decision Explanation</h2>

            <h3>
                Prediction:
                <span> {explanation.prediction}</span>
            </h3>

            <p>
                <strong>
                    Confidence: {explanation.confidence}%
                </strong>
            </p>

            <hr />

            <h3>Summary</h3>

            <p>
                {explanation.summary}
            </p>

            <h3>Clinical Finding</h3>

            <p>
                {explanation.finding}
            </p>

            <h3>Recommendation</h3>

            <p>
                {explanation.recommendation}
            </p>

            <h3>Important ECG Regions</h3>

            <div>

                {
                    explanation.important_regions.map((region, index) => (

                        <span
                            key={index}
                            className="region-box"
                        >
                            {region}
                        </span>

                    ))
                }

            </div>

        </div>

    );

}

export default AIExplanation;