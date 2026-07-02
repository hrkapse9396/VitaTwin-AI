function HealthTimeline({history}){


return(

<div className="card timeline-card">


<h2>
Health Timeline
</h2>



<div className="timeline">


{

history.map((item,index)=>(


<div 
className="timeline-item"
key={index}
>



<div className="timeline-dot">

</div>



<div className="timeline-content">


<h3>

{item.prediction}

</h3>



<p>

Confidence:
<strong>
 {item.confidence}%
</strong>

</p>



<p>

Risk Level:

<span 
className={
item.risk_level === "HIGH RISK"
?
"risk-badge high"
:
item.risk_level === "MEDIUM RISK"
?
"risk-badge medium"
:
"risk-badge low"
}

>

{item.risk_level}

</span>


</p>




<p className="timeline-date">


{

item.date

?

new Date(item.date)
.toLocaleString()

:

"Recent Prediction"

}


</p>



</div>


</div>



))


}



</div>


</div>


)


}


export default HealthTimeline;