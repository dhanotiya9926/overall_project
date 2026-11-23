from fastapi import FastAPI
app=FastAPI()

@app.get("/signup")
def signup():
    return {
        "Message":"Signed up successfully"
    }