function PatientCard({patient}){


return(

<div className="card patient-card">


<div className="card-header">

<h2>
Patient Profile
</h2>

</div>



<div className="patient-info">


<div className="info-box">

<span>
Name
</span>

<h3>
{patient.name}
</h3>

</div>



<div className="info-box">

<span>
Age
</span>

<h3>
{patient.age} Years
</h3>

</div>




<div className="info-box">

<span>
Gender
</span>

<h3>
{patient.gender}
</h3>

</div>





<div className="info-box">

<span>
Patient ID
</span>

<h3>
#{patient.id}
</h3>

</div>



</div>


</div>

)


}


export default PatientCard;