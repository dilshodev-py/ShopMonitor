from pydantic import BaseModel


class CategoryForm(BaseModel):
    name: str
    parent_id: str


class OrderItemForm(BaseModel):
    quantity: int
