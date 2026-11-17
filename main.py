from fastapi import FastAPI
from database import Base,engine
from models import User


app=FastAPI()

@app.get("/")
def home():
    return{
        "MESSAGE":"WELCOME TO THE JOURNEY OF BACKEND"
    }
Base.metadata.create_all(bind=engine)