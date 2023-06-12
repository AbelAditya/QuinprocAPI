from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    Name: str
    PID: str

app = FastAPI()
client = MongoClient("mongodb+srv://abel:65r7PNLqDF8gHUQ0@testing.iylygdv.mongodb.net/?retryWrites=true&w=majority")

db = client.get_database("One")
UserData = db.UserData
collection = db.Beats

@app.get("/")
def home():
    return "This is home"


@app.get("/Login")
def Login(uname: str="", PID: int=0):
    if(UserData.find_one({"Name":uname,"PatientID":PID})!=None):
        data = {'Login':True}

    else:
        data = {"Login":False}
    return data

@app.post("/SignUp")
def signup(user: User):
    UserData.insert_one({"Name":user.Name,"PatientID":user.PID})

    return {"SignUp":True}

@app.get("/getBPM")
def getBPM(id: int=4817):
    x = collection.find_one({"ID":id})
    return {"ID":x['ID'],"BPM":x["BPM"]}
