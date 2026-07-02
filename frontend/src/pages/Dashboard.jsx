import { useEffect, useState } from "react";

import API from "../services/api";

import PatientCard from "../components/PatientCard";
import RiskCard from "../components/RiskCard";
import PredictionHistory from "../components/PredictionHistory";
import ECGChart from "../components/ECGChart";
import HealthSummary from "../components/HealthSummary";
import HealthTimeline from "../components/HealthTimeline";
import RiskTrend from "../components/RiskTrend";
import AIExplanation from "../components/AIExplanation";
import ModelPerformance from "../components/ModelPerformance";

import AIClinicalSummary from "../components/AIClinicalSummary";
import AIRecommendation from "../components/AIRecommendation";

function Dashboard(){


const [patients,setPatients]=useState([]);


const [patientId,setPatientId]=useState(1);


const [data,setData]=useState(null);


const [ecgLength,setEcgLength]=useState(0);


const [explanation,setExplanation]=useState(null);



useEffect(()=>{


API.get("/patients/")


.then((response)=>{


setPatients(response.data);


})


.catch((error)=>{


console.log(
"Patient API Error:",
error
);


});


},[]);







useEffect(()=>{


API.get(
`/patients/${patientId}/dashboard`
)


.then((response)=>{


setData(response.data);


})


.catch((error)=>{


console.log(
"Dashboard Error:",
error
);


});


},[patientId]);


useEffect(()=>{


API.get(
`/patients/${patientId}/explanation`
)


.then((response)=>{


setExplanation(response.data);


})


.catch((error)=>{


console.log(
"Explanation Error:",
error
);


});


},[patientId]);




if(!data){


return(

<div className="loading-screen">

<h2>
Loading Patient Health Twin...
</h2>

</div>

)


}







return(


<div className="dashboard">





<header className="dashboard-header">


<div className="logo-section">


<h1>
❤️ VitaTwin AI
</h1>


<p>
AI Powered Cardiac Health Monitoring System
</p>


</div>




<div className="system-status">

● System Active

</div>


</header>







<div className="patient-selector">


<label>

Select Patient:

</label>


<select

value={patientId}

onChange={
(e)=>
setPatientId(Number(e.target.value))
}

>


{

patients.map((patient)=>(


<option

key={patient.id}

value={patient.id}

>

{patient.name}


</option>


))


}


</select>


</div>









<div className="page-title">


<h2>

Patient Health Twin Dashboard

</h2>


<p>

Real-time cardiac health analysis and prediction

</p>


</div>








<div className="top-grid">



<PatientCard

patient={data.patient}

/>




<RiskCard

prediction={data.latest_prediction}

/>

<AIClinicalSummary

patient={data.patient}

prediction={data.latest_prediction}

explanation={explanation}

/>

<AIRecommendation

prediction={data.latest_prediction}

/>

</div>







<HealthSummary


summary={data.health_summary}


prediction={data.latest_prediction}


ecgLength={ecgLength}


/>









<ECGChart

patientId={patientId}

setEcgLength={setEcgLength}

/>



<ModelPerformance />






<PredictionHistory

history={data.history}

/>

<HealthTimeline

history={data.history}

/>

{

explanation &&

<AIExplanation

explanation={explanation}

/>

}

<RiskTrend

history={data.history}

/>

</div>


)


}



export default Dashboard;