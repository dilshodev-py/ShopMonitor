from fastapi import FastAPI

from db.models import Category, OrderItem
from db.models import Order
from db.sessions import SessionDep
from forms import CategoryForm, OrderItemForm
from utils import update

app = FastAPI()


@app.post('/order')
async def create_order(pk: int, session: SessionDep):
    new_order = Order(**dict(Order))
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)
    return {"message": f"pk = {pk} sonli zakaz qabul qilindi !"}


@app.post('/category')
async def create_category(category: CategoryForm, session: SessionDep):
    new_category = Category(**dict(category))
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return {"message": f" Successful {dict(new_category)}"}


@app.patch('/category/{category_id}')
async def update_category(category_id: int, session: SessionDep, form: CategoryForm):
    category = await session.get(Category, category_id)
    await update(form, category)
    await session.commit()
    await session.refresh(category)
    return category


@app.patch('/orderItem/{id}')
async def update_orderItem(id: int, session: SessionDep, form: OrderItemForm):
    orderItem = await session.get(OrderItem, id)
    await update(form, orderItem)
    await session.commit()
    await session.refresh(orderItem)
    return orderItem
