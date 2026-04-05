from fastapi import FastAPI
import models
from database import engine
from routes import transactions

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Backend API",
    description="Backend system for managing financial transactions with role-based access",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Finance API is running"}

app.include_router(transactions.router, prefix="/api")