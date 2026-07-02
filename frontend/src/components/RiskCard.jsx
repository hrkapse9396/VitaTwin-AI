function RiskCard({prediction}){


let riskClass="";
let riskIcon="";
let riskMessage="";


if(prediction.risk_level==="HIGH RISK")
{

    riskClass="risk-high";

    riskIcon="🔴";

    riskMessage="Immediate cardiac attention recommended";

}

else if(prediction.risk_level==="MEDIUM RISK")
{

    riskClass="risk-medium";

    riskIcon="🟠";

    riskMessage="Regular monitoring recommended";

}

else
{

    riskClass="risk-low";

    riskIcon="🟢";

    riskMessage="No major abnormality detected";

}



let confidenceText="";


if(prediction.confidence >= 80)
{
    confidenceText="High confidence prediction";
}
else if(prediction.confidence >=50)
{
    confidenceText="Moderate confidence prediction";
}
else
{
    confidenceText="Low confidence prediction";
}



return(

<div className="card risk-card">



<h2>
Cardiac Risk Assessment
</h2>





<div className="risk-result">


<h1>
{prediction.prediction}
</h1>


<p>
AI Detection Result
</p>


</div>






<div className="confidence">


<h3>
Prediction Confidence
</h3>



<div className="progress-container">


<div

className="progress-bar"

style={{
width:`${prediction.confidence}%`
}}

>

</div>


</div>




<h2>
{prediction.confidence.toFixed(2)}%
</h2>



<p>

{confidenceText}

</p>



</div>







<div className={riskClass}>


<h1>

{riskIcon}

{" "}

{prediction.risk_level}

</h1>



<p>

{riskMessage}

</p>


</div>






</div>

)


}


export default RiskCard;