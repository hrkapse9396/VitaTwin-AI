function AIClinicalSummary({patient, prediction, explanation}){


return(

<div className="card clinical-summary">


<h2>
🩺 AI Clinical Summary
</h2>



<div className="summary-item">

<h3>
Patient
</h3>

<p>
{patient.name}
</p>

</div>




<div className="summary-item">

<h3>
Prediction
</h3>

<p>
{prediction.prediction}
</p>

</div>





<div className="summary-item">

<h3>
Confidence
</h3>

<p>
{prediction.confidence.toFixed(2)}%
</p>

</div>





<div className="summary-item">

<h3>
Risk Level
</h3>

<p>
{prediction.risk_level}
</p>

</div>





<div className="summary-item">


<h3>
AI Observation
</h3>


{

explanation?.explanations?.map(

(item,index)=>(

<p key={index}>
• {item}
</p>

)

)

}



</div>



</div>

)


}


export default AIClinicalSummary;