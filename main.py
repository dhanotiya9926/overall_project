from fastapi import FastAPI
from database2 import Base,engine
from models3 import User
from router import auth5


app=FastAPI()


@app.get("/")
def home():
    return{
        "MESSAGE":"WELCOME TO The First Docker File"
    }
app.include_router(auth5.router)
Base.metadata.create_all(bind=engine)