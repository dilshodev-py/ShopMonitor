from fastapi import FastAPI
from db.config import SessionDep
from db.models import Ingradient, Category, OrderItem, Order
from forms import IngredientForm
from schemas import CategoryForm, OrderItemForm
from utils import update

app = FastAPI()


@app.post('/save/ingredients/')
async def save_ingredients(session:SessionDep,form:IngredientForm):
    ingredient=await Ingradient.create(session,**dict(form))
    return ingredient

@app.post("/category")
async def category_create(category: CategoryForm, session: SessionDep):
    new_category = Category(**dict(category))
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return dict(new_category)


@app.delete('/order/delete/{order_id}', tags=['order'])
async def order_delete(order_id: int, session: SessionDep):
    order = await session.get(Order, order_id)
    await session.delete(order)
    await session.commit()
    return {'message': 'Order deleted successfully!'}


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
