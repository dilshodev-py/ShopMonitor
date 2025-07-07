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

@app.patch('/category/{category_id}')
async def update_category(category_id: int, session: SessionDep, form: CategoryForm):
    category = await session.get(Category, category_id)
    await update(category, form)
    await session.commit()
    await session.refresh(category)
    return category


@app.patch('/orderItem/{id}')
async def update_orderItem(id: int, session: SessionDep, form: OrderItemForm):
    orderItem = await session.get(OrderItem, id)
    await update(orderItem, form)
    await session.commit()
    await session.refresh(orderItem)
    return orderItem
