import pytest
from httpx import AsyncClient

from conf_test_db import app
from tests.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_new_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        payload = {
            "name": "Quaker Oats",
            "quantity": 10,
            "description": "Quaker Oats is a brand of rolled oats",
            "price": 10.00,
            "category_id": category_obj.id,
        }
        response = await ac.post("/products/", json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Quaker Oats"
    assert response.json()["description"] == "Quaker Oats is a brand of rolled oats"
    assert response.json()["price"] == 10.00
    assert response.json()["category_id"] == category_obj.id


@pytest.mark.asyncio
async def test_list_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        category_obj = await category_info()
        product_obj = await product_info(category_obj)
        response = await ac.get("/products/")
    assert response.status_code == 200
    assert response.json()[0]["name"] == product_obj.name
    assert response.json()[0]["description"] == product_obj.description
    assert response.json()[0]["price"] == product_obj.price
    assert response.json()[0]["quantity"] == 10
