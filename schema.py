from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    code: str
    nomi: str
    images: List[str]
    thumbnail: str
    quantity: int
    discount: Optional[float] = 0
    sell_price: float
    arrive_price: float
    percentage: Optional[float] = 0
    category_id: int

class ProductResponse(BaseModel):
    id: str
    code: str
    nomi: str
    images: List[str]
    thumbnail: str
    quantity: int
    discount: float
    sell_price: float
    arrive_price: float
    percentage: float
    profit_amount: float
    category_id: int
    status: str
    created_at: str
    updated_at: str