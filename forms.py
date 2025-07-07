from pydantic import BaseModel


class IngredientForm(BaseModel):
    name: str



class ProductIngredientForm(BaseModel):
    product_id:int|None=None
    ingredient_id:int|None=None
    value:float|None=None
    portion:str|None=None
