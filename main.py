from fastapi import FastAPI
import models
from database import engine
from routes import transactions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Finance Backend API",
    description="Backend system for managing financial transactions with role-based access",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Finance API is running"}


app.include_router(transactions.router, prefix="/api")
