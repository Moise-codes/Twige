from fastapi import FastAPI , HTTPException

from pydantic import BaseModel


app = FastAPI(
  title = "Twige API",
  description = "Twige School Management Information System",
  version = "1.0.0"


)

@app.get("/")
def home():
  return {
    "message" : "Welcome to Twige SchoolMIS",
    "status" : "running"
  }

schools = [
    {
      "id" : 1,
      "name" : "Rwanda Coding Academy",
      "location" : "Nyabihu",
      "email" : "rca@ac.rw"
    },

    {
      "id" : 2,
      "name" : "Kagarama SS",
      "location" : "Kigali",
      "email" : "kagarama@co"
    }

  ]

@app.get("/api/v1/schools")
def get_schools():
    return {
     "total" : len(schools),
      "schools" :  schools
    }



@app.get("/api/v1/schools/{school_id}")
def get_school(school_id : int ):
  for school in schools :

    if school_id == school["id"] :
      return {
        "school" : school
      }

  raise HTTPException(
          status_code  = 404,
          detail = "School not found"
        )



class SchoolCreate(BaseModel):
  name : str
  location : str
  email : str



@app.post("/api/v1/schools",status_code = 201)
def create_school(school : SchoolCreate):
  new_school = school.model_dump()
  new_school["id"] = len(schools) + 1
  schools.append(new_school)
  return new_school



class SchoolUpdate(BaseModel):
 name : str
 location : str
 email : str



@app.put("/api/v1/schools/{school_id}")

def update_school(school_id : int , updated_school : SchoolUpdate):
  for school in schools:
     school["id"] == school_id
     new_data = updated_school.model_dump()

     school.update(new_data)

     return school

     raise HTTPException(

      status_code = 404,
      detail = "School not found"
     )




@app.delete("/api/v1/schools/{school_id}")
def delete_school(school_id : int):
 for school in schools:
  if school["id"] == school_id:
    schools.remove(school)

    return {

      "message" : "School deleted successfully!"
    }

  raise HTTPException(
    status_code = 404,
    detail = "School not found"
  )
