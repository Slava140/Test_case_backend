from pydantic import BaseModel, PositiveInt, Field


class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    price: PositiveInt


class ProductWithoutID(ProductBase):
    ...


class ProductWithID(ProductBase):
    id: PositiveInt
