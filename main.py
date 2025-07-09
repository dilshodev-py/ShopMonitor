from fastapi import FastAPI

from db.models import Category, OrderItem
from db.models import Order
from db.sessions import SessionDep
from forms import CategoryForm, OrderItemForm, OrderForm
from utils import update

app = FastAPI()


@app.patch('/category/{category_id}', tags=['category'])
async def update_category(category_id: int, session: SessionDep, form: CategoryForm):
    category = await session.get(Category, category_id)
    await update(form, category)
    await session.commit()
    await session.refresh(category)
    return category


@app.patch('/orderItem/{id}', tags=['order'])
async def update_order_item(id: int, session: SessionDep, form: OrderItemForm):
    order_item = await session.get(OrderItem, id)
    await update(form, order_item)
    await session.commit()
    await session.refresh(order_item)
    return order_item


@app.post('/category', tags=['category'])
async def create_category(category: CategoryForm, session: SessionDep):
    new_category = Category(**dict(category))
    session.add(new_category)
    await session.commit()
    await session.refresh(new_category)
    return {"message": f" Successful {dict(new_category)}"}


@app.post("/category", tags=['category'])
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


@app.post('/order', tags=['order'])
async def create_order(session: SessionDep, order: OrderForm):
    order_items = [OrderItem(**dict(order)) for order in order.order_items]
    new_order = Order(
        total_price=order.total_price,
        order_items=order_items
    )
    session.add(new_order)
    await session.commit()
    await session.refresh(new_order)
    return {'id': new_order.id}
