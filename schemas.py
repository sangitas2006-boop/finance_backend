from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Literal, Optional

class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str = Field(min_length=1)
    date: date
    notes: Optional[str] = None


class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: Literal["income", "expense"]
    category: str
    date: date
    notes: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True