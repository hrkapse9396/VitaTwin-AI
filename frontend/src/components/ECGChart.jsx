import { useEffect, useState } from "react";

import API from "../services/api";

import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
    ReferenceArea
} from "recharts";


function ECGChart({patientId, setEcgLength}){
    console.log("ECG Patient ID:", patientId);


const [ecgData,setEcgData] = useState([]);

const [totalSamples,setTotalSamples] = useState(0);

const [importantRegions,setImportantRegions] = useState([]);





useEffect(()=>{


API.get(`/patients/${patientId}/ecg`)


.then((response)=>{


const values=response.data.ecg;



setTotalSamples(
    response.data.length
);



if(setEcgLength)
{

setEcgLength(
    response.data.length
);

}





const chartData=values

.slice(0,1250)

.map(

(value,index)=>(

{

time:index,

signal:value

}

)

);



setEcgData(chartData);



})



.catch((error)=>{


console.log(
"ECG ERROR:",
error
);


});



},[patientId,setEcgLength]);







useEffect(()=>{


API.get(`/patients/${patientId}/explanation`)


.then((response)=>{


console.log(
"Explanation:",
response.data
);



setImportantRegions(
response.data.important_regions
);



})


.catch((error)=>{


console.log(
"Explanation ERROR:",
error
);


});


},[patientId]);







return(


<div className="card ecg-card">



<h2>
ECG Waveform Analysis
</h2>





<div className="ecg-info">



<div>

<h3>
Signal Status
</h3>


<p className="normal-status">
AI Analysed ECG
</p>


</div>





<div>

<h3>
Total Samples
</h3>


<p>
{totalSamples}
</p>


</div>





<div>

<h3>
Displayed Points
</h3>


<p>
{ecgData.length}
</p>


</div>




</div>







{

ecgData.length===0

?

<p>
Loading ECG waveform...
</p>


:


<div className="chart-container">


<ResponsiveContainer

width="100%"

height={450}

>


<LineChart

data={ecgData}

>


<CartesianGrid/>


<XAxis

dataKey="time"

/>


<YAxis/>


<Tooltip/>




{

importantRegions.length === 2 &&

<ReferenceArea

x1={importantRegions[0]}

x2={importantRegions[1]}

fillOpacity={0.3}

/>

}




<Line

type="monotone"

dataKey="signal"

dot={false}

strokeWidth={2}

/>


</LineChart>

</ResponsiveContainer>



</div>



}





</div>



)


}



export default ECGChart;