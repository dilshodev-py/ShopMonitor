from pydantic import BaseModel


class IngredientForm(BaseModel):
    name: str
