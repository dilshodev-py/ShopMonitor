from datetime import datetime
import uuid

from fastapi import FastAPI, HTTPException

from schema import ProductResponse, ProductCreate

app = FastAPI()

#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}


#DATA
products_db = {}


@app.post("/api/v1/product", response_model=ProductResponse)
async def create_product(product: ProductCreate):
    for existing_product in products_db.values():
        if existing_product["code"] == product.code:
            raise HTTPException(status_code=400, detail="Bu kod allaqachon mavjud")

    product_id = str(uuid.uuid4())
    current_time = datetime.now().isoformat()

    new_product = {
        "id": product_id,
        "code": product.code,
        "nomi": product.nomi,
        "images": product.images,
        "thumbnail": product.thumbnail,
        "quantity": product.quantity,
        "discount": product.discount,
        "sell_price": product.sell_price,
        "arrive_price": product.arrive_price,
        "percentage": product.percentage,
        "profit_amount": product.sell_price - product.arrive_price,
        "category_id": product.category_id,
        "status": "active" if product.quantity > 0 else "out_of_stock",
        "created_at": current_time,
        "updated_at": current_time
    }

    products_db[product_id] = new_product
    return ProductResponse(**new_product)