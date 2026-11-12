from fastapi import FastAPI , HTTPException

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
