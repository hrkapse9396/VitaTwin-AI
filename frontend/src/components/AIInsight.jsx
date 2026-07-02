import { useEffect, useState } from "react";

import API from "../services/api";


function AIInsight(){


const [insight,setInsight] = useState(null);



useEffect(()=>{


API.get("/patients/1/explanation")


.then((response)=>{


console.log(
"AI Explanation:",
response.data
);


setInsight(
response.data
);


})


.catch((error)=>{


console.log(
"AI Insight Error:",
error
);


});


},[]);






return(


<div className="card ai-card">


<h2>
AI Clinical Insights
</h2>




{

!insight

?

<p>
Loading AI analysis...
</p>


:


<>


<div className="insight-box">


<h3>
Prediction
</h3>


<p>
{insight.prediction}
</p>


</div>






<div className="insight-box">


<h3>
Confidence
</h3>


<p>
{insight.confidence.toFixed(2)}%
</p>


</div>







<div className="insight-box">


<h3>
Risk Level
</h3>


<p>
{insight.risk_level}
</p>


</div>






<div className="explanation-section">


<h3>
AI Explanation
</h3>



<ul>


{

insight.explanations.map(

(item,index)=>(


<li key={index}>

{item}

</li>


)


)


}


</ul>


</div>






<div className="region-section">


<h3>
Important ECG Regions
</h3>


<p>

Samples:

{insight.important_regions[0]}

-

{insight.important_regions[1]}

</p>


</div>




</>


}



</div>


)


}


export default AIInsight;