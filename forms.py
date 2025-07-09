from typing import Optional

from pydantic import BaseModel


class IngredientForm(BaseModel):
    name: str


class CategoryForm(BaseModel):
    name: str
    parent_id: Optional[int]


class OrderItemForm(BaseModel):
    quantity: int


class OrderForm(BaseModel):
    total_price: float
    order_items: list[OrderItemForm]


class ProductIngredientForm(BaseModel):
    product_id: int | None = None
    ingredient_id: int | None = None
    value: float | None = None
    portion: str | None = None
