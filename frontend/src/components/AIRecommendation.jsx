function AIRecommendation({prediction}){


let message="";


if(prediction.risk_level==="HIGH RISK")
{

message=[
"Immediate cardiac consultation recommended",
"Continuous ECG monitoring advised",
"Further clinical investigation required"
];

}


else if(prediction.risk_level==="MEDIUM RISK")
{

message=[
"Regular cardiac monitoring recommended",
"Follow-up evaluation suggested",
"Maintain healthy lifestyle practices"
];

}


else
{

message=[
"Continue regular health monitoring",
"Maintain current lifestyle habits"
];

}




return(

<div className="card recommendation-card">


<h2>
🧠 AI Health Recommendation
</h2>


<ul>

{

message.map(

(item,index)=>(

<li key={index}>
{item}
</li>

)

)

}

</ul>


</div>

)

}


export default AIRecommendation;