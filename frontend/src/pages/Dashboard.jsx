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
import ECGUpload from "../components/ECGUpload";

import HealthIntelligence from "../components/HealthIntelligence";
import PatientTwin from "../components/PatientTwin";

function Dashboard(){


const [patients,setPatients]=useState([]);


const [patientId,setPatientId]=useState(1);


const [data,setData]=useState(null);


const [ecgLength,setEcgLength]=useState(0);


const [explanation,setExplanation]=useState(null);
const [intelligence,setIntelligence]=useState(null);
const [patientTwin,setPatientTwin]=useState(null);
const loadDashboard = () => {

    API.get(`/patients/${patientId}/dashboard`)

        .then((response) => {

            setData(response.data);

        })

        .catch((error) => {

            console.log("Dashboard Error:", error);

        });

};

const loadExplanation = () => {

    API.get(`/patients/${patientId}/explanation`)

        .then((response) => {

            setExplanation(response.data);

        })

        .catch((error) => {

            console.log("Explanation Error:", error);

        });

};


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



useEffect(() => {

    loadDashboard();

}, [patientId]);


useEffect(() => {

    loadExplanation();

}, [patientId]);

const loadHealthIntelligence = () => {

    API.get(`/patients/${patientId}/health-intelligence`)

        .then((response) => {

            setIntelligence(response.data);

        })

        .catch((error) => {

            console.log("Health Intelligence Error:", error);

        });

};

useEffect(() => {

    loadHealthIntelligence();

}, [patientId]);
const loadPatientTwin = () => {

    API.get(`/patients/${patientId}/patient-twin`)

        .then((response) => {

            setPatientTwin(response.data);

        })

        .catch((error) => {

            console.log("Patient Twin Error:", error);

        });

};
useEffect(() => {

    loadPatientTwin();

}, [patientId]);

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

<h2 className="section-title">
    ECG Analysis
</h2>
<ECGUpload
    patientId={patientId}
    onUploadSuccess={() => {
        loadDashboard();
        loadExplanation();
        loadHealthIntelligence();
        loadPatientTwin();
    }}
/>

<div className="page-title">



</div>

<div className="page-title">

<h2>

Patient Health Twin Dashboard

</h2>


<p>

Real-time cardiac health analysis and prediction

</p>


</div>






{/* ================= Patient Overview ================= */}

<h2 className="section-title">
    Patient Overview
</h2>

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

{/* ================= AI Health Intelligence ================= */}

<h2 className="section-title">
    AI Health Intelligence
</h2>

<div className="top-grid">

    <HealthSummary
        summary={data.health_summary}
        prediction={data.latest_prediction}
        ecgLength={ecgLength}
    />

    <HealthIntelligence
        intelligence={intelligence}
    />

    <PatientTwin
        twin={patientTwin}
    />

</div>


{/* ================= ECG Analysis ================= */}


<ECGChart
    patientId={patientId}
    setEcgLength={setEcgLength}
/>

{
    explanation &&
    <AIExplanation
        explanation={explanation}
    />
}



{/* ================= AI Model ================= */}

<h2 className="section-title">
    AI Model Performance
</h2>

<ModelPerformance />




{/* ================= Prediction Analytics ================= */}

<h2 className="section-title">
    Prediction Analytics
</h2>

<PredictionHistory
    history={data.history}
/>

<HealthTimeline
    history={data.history}
/>

<RiskTrend
    history={data.history}
/>

</div>


)


}



export default Dashboard;