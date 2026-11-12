from fastapi import FastAPI

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
