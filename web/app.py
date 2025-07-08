from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_admin.contrib.sqla import Admin, ModelView
from web.provider import UsernameAndPasswordProvider
from db import engine
from db.models import Category, Product, ProductImage, Order, OrderItem, ProductIngradient, Ingradient

app = Starlette()
admin = Admin(engine=engine,
              title='P_29Admin',
              base_url='/',
              auth_provider=UsernameAndPasswordProvider(),
              middlewares=[Middleware(SessionMiddleware, secret_key="sdgfhjhhsfdghn")]
              )

admin.add_view(ModelView(Category))
admin.add_view(ModelView(Product))
admin.add_view(ModelView(ProductImage))
admin.add_view(ModelView(Order))
admin.add_view(ModelView(OrderItem))
admin.add_view(ModelView(ProductIngradient))
admin.add_view(ModelView(Ingradient))
admin.mount_to(app)
