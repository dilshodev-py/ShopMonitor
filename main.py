from fastapi import FastAPI

from db.models import Category, OrderItem
from db.sessions import SessionDep
from schemas import CategoryForm, OrderItemForm
from utils import update

app = FastAPI()


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
