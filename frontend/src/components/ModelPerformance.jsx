import { useEffect, useState } from "react";

import API from "../services/api";


function ModelPerformance(){


const [performance,setPerformance] = useState(null);




useEffect(()=>{


API.get("/performance/")


.then((response)=>{


console.log(
"Performance API:",
response.data
);


setPerformance(
response.data
);


})


.catch((error)=>{


console.log(
"Performance ERROR:",
error
);


});


},[]);






return(


<div className="card">


<h2>
Model Performance
</h2>



{

!performance

?

<p>
Loading performance metrics...
</p>


:


<>



<div className="performance-container">



<div className="metric-card">

<h3>
Accuracy
</h3>

<p>
{performance.accuracy}%
</p>

</div>





<div className="metric-card">

<h3>
Precision
</h3>

<p>
{performance.precision}%
</p>

</div>





<div className="metric-card">

<h3>
Recall
</h3>

<p>
{performance.recall}%
</p>

</div>





<div className="metric-card">

<h3>
F1 Score
</h3>

<p>
{performance.f1_score}%
</p>

</div>



</div>





<h3>
Confusion Matrix
</h3>



<table>


<thead>

<tr>

<th></th>

<th>
AFIB
</th>

<th>
NORMAL
</th>

</tr>

</thead>




<tbody>


<tr>

<td>
Actual AFIB
</td>


<td>
{performance.confusion_matrix.true_positive}
</td>


<td>
{performance.confusion_matrix.false_negative}
</td>


</tr>





<tr>

<td>
Actual NORMAL
</td>


<td>
{performance.confusion_matrix.false_positive}
</td>


<td>
{performance.confusion_matrix.true_negative}
</td>


</tr>



</tbody>


</table>



</>

}



</div>


)


}


export default ModelPerformance;