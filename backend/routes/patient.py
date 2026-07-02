from fastapi import APIRouter


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)



patients = [

    {
        "id":1,
        "name":"Rahul",
        "age":49,
        "gender":"male"
    },

    {
        "id":2,
        "name":"Amit",
        "age":62,
        "gender":"male"
    },

    {
        "id":3,
        "name":"Priya",
        "age":45,
        "gender":"female"
    }

]



@router.get("/")
def get_patients():

    return patients