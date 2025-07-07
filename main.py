from fastapi import FastAPI
from db.config import SessionDep
from db.models import Ingradient
from forms import IngredientForm

app = FastAPI()


@app.post('/save/ingredients/')
async def save_ingredients(session:SessionDep,form:IngredientForm):
    ingredient=await Ingradient.create(session,**dict(form))
    return ingredient

@app.post("/category")
async def create_category(pk: int, name: str):
    return {
        "id": pk,
        "name": category.name,
        "message": "Category created"
    }

@app.delete("/order")
async def delete_order(pk: int):
    return {
        "id": pk,
        "message": "Order deleted"
    }
