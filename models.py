from sqlalchemy import Column, Integer, String, Float, Date, DateTime, CheckConstraint
from sqlalchemy.sql import func
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable=False)

    type = Column(String, nullable=False)  # income or expense

    category = Column(String, nullable=False)

    date = Column(Date, nullable=False)

    notes = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        CheckConstraint("amount > 0", name="check_amount_positive"),
        CheckConstraint("type IN ('income', 'expense')", name="check_type_valid"),
    )