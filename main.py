from fastapi import FastAPI
from db.config import SessionDep
from db.models import Ingradient
from forms import IngredientForm

app = FastAPI()


@app.post('/save/ingredients/')
async def save_ingredients(session:SessionDep,form:IngredientForm):
    ingredient=await Ingradient.create(session,**dict(form))
    return ingredient