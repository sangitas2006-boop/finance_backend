from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import schemas
import models
from services import transaction_service
from services.auth_service import require_role
from typing import Literal

type: Literal["income", "expense"] = None

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(
    transaction: schemas.TransactionCreate,
    role: str,
    db: Session = Depends(get_db)
):
    require_role(role, ["admin"])
    return transaction_service.create_transaction(db, transaction.dict())


@router.get("/transactions/", response_model=list[schemas.TransactionResponse])
def get_transactions(role: str, db: Session = Depends(get_db)):
    require_role(role, ["admin", "analyst", "viewer"])
    return transaction_service.get_all_transactions(db)


@router.get("/transactions/filter/", response_model=list[schemas.TransactionResponse])
def filter_transactions(
    role: str,
    type: Literal["income", "expense"] = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    require_role(role, ["admin", "analyst"])
    return transaction_service.filter_transactions(db, type, category)


@router.get("/summary/")
def summary(role: str, db: Session = Depends(get_db)):
    require_role(role, ["admin", "analyst"])
    return transaction_service.get_summary(db)