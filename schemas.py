from pydantic import BaseModel


class CategoryForm(BaseModel):
    name: str = None
    parent_id: str = None


class OrderItemForm(BaseModel):
    quantity: int
