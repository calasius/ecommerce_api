import pytest
from httpx import AsyncClient

from ecommerce.auth.jwt import create_access_token
from conf_test_db import app
from tests.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_add_to_cart():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})
        category_obj = await category_info()
        product_obj = await product_info(category_obj)

        response = await ac.get(
            "/cart/add",
            params={"product_id": product_obj.id},
            headers={"Authorization": f"Bearer {user_access_token}"},
        )

    assert response.status_code == 201
    assert response.json() == {"status": "Item added to cart"}


@pytest.mark.asyncio
async def test_cart_listing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "john@gmail.com"})
        response = await ac.get(
            "/cart/", headers={"Authorization": f"Bearer {user_access_token}"}
        )
    assert response.status_code == 200
