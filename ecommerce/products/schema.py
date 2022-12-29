from pydantic import BaseModel, constr
from typing import Optional


class Category(BaseModel):
    name: constr(min_length=2, max_length=50)


class ListCategory(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    id: Optional[int]
    name: str
    price: float
    description: str
    quantity: int
    category_id: int

    class Config:
        orm_mode = True


class Product(ProductBase):
    category_id: int


class ProductListing(ProductBase):
    category: ListCategory

    class Config:
        orm_mode = True
