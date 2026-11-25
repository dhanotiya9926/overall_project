
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

# Database imports
from database2 import Base, engine

# Router imports
from router import auth5


# Initialize FastAPI
app = FastAPI()


# Project directory
BASE_DIR = Path(__file__).resolve().parent


# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Serve CSS and JavaScript files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# Frontend Home Page
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


# Include Authentication Router
app.include_router(auth5.router)


# Create Database Tables
Base.metadata.create_all(bind=engine)