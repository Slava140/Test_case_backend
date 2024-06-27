from typing import Mapping

from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from src.database import engine
from src.models import Product as ProductModel


class ProductsRepository:
    @staticmethod
    def is_id_exists(product_id: int) -> bool:
        with Session(engine) as session:
            query = select(ProductModel.id).where(ProductModel.id == product_id)
            result = session.execute(query).scalar_one_or_none()
            return result is not None

    @staticmethod
    def create(data: Mapping) -> dict | None:
        with Session(engine) as session:
            stmt = insert(
                ProductModel
            ).values(
                **data
            ).returning(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return dict(data) if data is not None else None

    @staticmethod
    def read(product_id: int) -> dict:
        with Session(engine) as session:
            query = select(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price
            ).where(
                ProductModel.id == product_id
            )
            data = session.execute(query).mappings().one_or_none()
        return dict(data) if data is not None else None

    @staticmethod
    def read_many(limit: int, offset: int) -> list[dict] | None:
        with Session(engine) as session:
            query = select(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price
            ).limit(limit).offset(offset)
            data = session.execute(query).mappings().all()
        return [dict(product_data) for product_data in data] if data else None

    @staticmethod
    def update(product_id: int, data: Mapping) -> dict:
        with Session(engine) as session:
            stmt = update(
                ProductModel
            ).where(
                ProductModel.id == product_id
            ).values(
                **data
            ).returning(
                ProductModel.id,
                ProductModel.name,
                ProductModel.price
            )
            data = session.execute(stmt).mappings().one_or_none()
            session.commit()
        return dict(data) if data is not None else None

    @staticmethod
    def delete(product_id: int) -> None:
        with Session(engine) as session:
            stmt = delete(ProductModel).where(ProductModel.id == product_id)
            session.execute(stmt)
            session.commit()


products_repository = ProductsRepository()
