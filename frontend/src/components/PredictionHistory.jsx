function PredictionHistory({history}){


return(

<div className="card history-card">


<h2>
Prediction History
</h2>



<div className="table-container">


<table>


<thead>


<tr>

<th>
Prediction
</th>


<th>
Confidence
</th>


<th>
Risk Level
</th>


<th>
Date
</th>


</tr>


</thead>





<tbody>



{

history.map((item,index)=>{


let riskClass="";


if(item.risk_level==="HIGH RISK")
{

riskClass="risk-badge high";

}

else if(item.risk_level==="MEDIUM RISK")
{

riskClass="risk-badge medium";

}

else
{

riskClass="risk-badge low";

}



return(


<tr key={index}>


<td>

<span className="prediction-name">

{item.prediction}

</span>

</td>




<td>

{item.confidence}%

</td>





<td>

<span className={riskClass}>

{item.risk_level}

</span>


</td>





<td>

{

item.date

?

new Date(item.date)
.toLocaleDateString()

:

"Recent"

}


</td>




</tr>


)



})


}



</tbody>



</table>



</div>



</div>


)


}


export default PredictionHistory;