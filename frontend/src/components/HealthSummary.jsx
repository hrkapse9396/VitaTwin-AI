function HealthSummary({
    summary,
    prediction,
    ecgLength
}){


return(

<div className="card">


<h2>
Health Summary
</h2>



<div className="summary-grid">


<div className="summary-box">

<div className="summary-icon">
📊
</div>


<h3>
Total Predictions
</h3>


<h1>
{
summary?.total_predictions || 0
}
</h1>


</div>




<div className="summary-box">

<div className="summary-icon">
❤️
</div>


<h3>
Rhythm Status
</h3>


<h1 className="afib-status">

{
summary?.afib_detected
?
"AFIB FOUND"
:
"NORMAL"
}

</h1>


</div>





<div className="summary-box">

<div className="summary-icon">
🎯
</div>


<h3>
Confidence Score
</h3>


<h1>
{prediction.confidence}%
</h1>


</div>





<div className="summary-box">

<div className="summary-icon">
📈
</div>


<h3>
ECG Samples
</h3>


<h1>
{ecgLength || 0}
</h1>


</div>



</div>


</div>

)


}


export default HealthSummary;