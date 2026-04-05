from sqlalchemy.orm import Session
import models
from sqlalchemy import func

def create_transaction(db: Session, data):
    try:
        transaction = models.Transaction(**data)
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        return transaction
    except Exception as e:
        db.rollback()
        raise e


def get_all_transactions(db: Session):
    return db.query(models.Transaction).all()


def get_summary(db: Session):
    total_income = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "income").scalar() or 0
    total_expense = db.query(func.sum(models.Transaction.amount)).filter(models.Transaction.type == "expense").scalar() or 0

    transactions = db.query(models.Transaction).all()

    category_breakdown = {}
    for t in transactions:
        category_breakdown[t.category] = category_breakdown.get(t.category, 0) + t.amount

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "category_breakdown": category_breakdown
    }