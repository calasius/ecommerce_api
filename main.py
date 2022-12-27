from fastapi import FastAPI
from ecommerce.user import router as user_router
from ecommerce.products import router as product_router
from ecommerce.cart import router as cart_router

app = FastAPI(title="EcommerceApp", version="0.0.1")

app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(cart_router.router)

