from typing import Optional

from pydantic import BaseModel


class IngredientForm(BaseModel):
    name: str


class CategoryForm(BaseModel):
    name: str
    parent_id: Optional[int]


class OrderItemForm(BaseModel):
    quantity: int


class ProductIngredientForm(BaseModel):
    product_id: int | None = None
    ingredient_id: int | None = None
    value: float | None = None
    portion: str | None = None
