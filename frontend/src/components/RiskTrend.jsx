import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer
} from "recharts";



function RiskTrend({history}){


const chartData = history.map(
(item,index)=>(

{

prediction:
`Record ${index+1}`,

risk:
item.risk_score || item.confidence

}

)

);





return(

<div className="card">


<h2>
Risk Trend Analysis
</h2>




{

chartData.length === 0

?

<p>
No risk data available
</p>


:


<div

style={{

width:"100%",

height:"350px"

}}

>


<ResponsiveContainer
width="100%"
height="100%"
>


<LineChart

data={chartData}

>


<CartesianGrid />



<XAxis

dataKey="prediction"

/>



<YAxis

domain={[0,100]}

/>



<Tooltip />



<Line

type="monotone"

dataKey="risk"

strokeWidth={3}

dot={true}

/>



</LineChart>


</ResponsiveContainer>


</div>


}



</div>


)


}


export default RiskTrend;