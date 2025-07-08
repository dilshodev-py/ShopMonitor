from fastapi import FastAPI
from db.config import SessionDep
from db.models import Ingradient, ProductIngradient
from forms import IngredientForm, ProductIngredientForm

app = FastAPI()


@app.post('/save/ingredients/')
async def save_ingredients(session: SessionDep, form: IngredientForm):
    ingredient = await Ingradient.create(session, **dict(form))
    return ingredient


@app.patch('/update/ingredients/<id>')
async def update_ingredients(session: SessionDep, form: IngredientForm, id: int):
    ingredient = await Ingradient.update(session, id, form)
    return ingredient


@app.get('/get/ingredients/')
async def get_ingredients(session: SessionDep):
    ingredients = await Ingradient.get_all(session)
    return ingredients


@app.post('/save/product/ingredients/')
async def save_product_ingredients(session: SessionDep, form: ProductIngredientForm):
    product_ingredient = await ProductIngradient.create(session, **dict(form))
    return product_ingredient


@app.get('/get/product/ingredients/')
async def get_product_ingredients(session: SessionDep):
    product_ingredients = await ProductIngradient.get_all(session)
    return product_ingredients


@app.patch('/update/products/ingredients/<id>')
async def update_ingredients(session: SessionDep, form: ProductIngredientForm, id: int):
    ingredient = await ProductIngradient.update(session, id, form)
    return ingredient
