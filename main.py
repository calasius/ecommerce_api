from fastapi import FastAPI
from celery import Celery
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router
from ecommerce.orders import router as order_router
from ecommerce import config

app = FastAPI(title="EcommerceApp", version="0.0.1")

app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)
app.include_router(order_router.router)

celery = Celery(
    __name__,
    broker=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
    backend=f"redis://{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}",
)

celery.conf.imports = [
    "ecommerce.orders.tasks",
]
