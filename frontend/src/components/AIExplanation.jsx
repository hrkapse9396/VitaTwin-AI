function AIExplanation({explanation}){


return(

<div className="card">


<h2>
AI Decision Explanation
</h2>



<h3>
Prediction:
<span>

 {explanation.prediction}

</span>
</h3>




<p>

Confidence:

<strong>
 {explanation.confidence}%

</strong>

</p>





<h3>
Why AI detected this?
</h3>



<ul>


{

explanation.explanations.map(

(reason,index)=>(


<li key={index}>

{reason}

</li>


)

)


}



</ul>





<h3>
Important ECG Regions
</h3>



<div>


{

explanation.important_regions.map(

(region,index)=>(


<span

key={index}

className="region-box"

>

{region}

</span>


)


)


}



</div>



</div>


)


}


export default AIExplanation;