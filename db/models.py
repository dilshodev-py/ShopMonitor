import asyncio
from sqlalchemy import String, Float, Integer, Boolean,DateTime
from sqlmodel import Field, SQLModel, Relationship

from db import engine
from db.config import CreatedModel


class Category(CreatedModel, table=True):
    __tablename__ = 'categories'
    name: str = Field(index=True,sa_type=String)
    parent_id: int  = Field(nullable=True, foreign_key="categories.id")
    category: list["Product"] = Relationship(back_populates="products")


class Product(CreatedModel, table=True):
    name: str = Field(index=True, sa_type=String)
    code: str = Field(nullable=True, sa_type=String)
    arrive_price: float = Field(default=0, sa_type=Float)
    sell_price: float = Field(default=0, sa_type=Float)
    percentage: int = Field(default=0, sa_type=Integer)
    discount: int = Field(default=0, sa_type=Integer)
    quantity: int = Field(default=0, sa_type=Integer)
    thumbnail: str = Field(default="", sa_type=String)
    is_avilable: bool = Field(default=False, sa_type=Boolean)
    category_id: int = Field(nullable=True, foreign_key="categories.id")
    products: "Category" = Relationship(back_populates="category")
    images: list["ProductImage"] = Relationship(back_populates="product")
    product_ingredients: list["ProductIngradient"] = Relationship(back_populates="product")
    order_items:list["OrderItem"]=Relationship(back_populates="product")


class ProductImage(CreatedModel, table=True):
    product_id: int = Field(nullable=True, foreign_key="products.id")
    title: str = Field(nullable=True, sa_type=String)
    image: str = Field(nullable=True, sa_type=String)
    product: "Product"= Relationship(back_populates="images")


class Ingradient(CreatedModel, table=True):
    name:str=Field(nullable=True,sa_type=String)
    product_ingredients: list["ProductIngradient"] = Relationship(back_populates="ingradient")


class ProductIngradient(CreatedModel, table=True):
    __tablename__ = "product_ingradient"

    ingredient_id: int = Field(nullable=True, foreign_key="ingradients.id")
    product_id: int = Field(nullable=True, foreign_key="products.id")
    product: "Product" = Relationship(back_populates="product_ingredients")
    ingradient: "Ingradient" = Relationship(back_populates="product_ingredients")
    value:float=Field(sa_type=Float,default=0)
    portion:str=Field(sa_type=String,nullable=True)


class Order(CreatedModel, table=True):
    total_price: float = Field(default=0, sa_type=Float)
    order_at:str=Field(nullable=True,sa_type=DateTime)
    order_items: list["OrderItem"] = Relationship(back_populates="order")


class OrderItem(CreatedModel, table=True):
    __tablename__ = 'order_items'

    product_id: int = Field(nullable=True, foreign_key="products.id")
    quantity: int = Field(default=0, sa_type=Integer)
    order_id: int = Field(nullable=True, foreign_key="orders.id")
    order: "Order" = Relationship(back_populates="order_items")
    product: "Product" = Relationship(back_populates="order_items")

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


metadata = SQLModel.metadata

if __name__ == "__main__":
    asyncio.run(create_db_and_tables())
