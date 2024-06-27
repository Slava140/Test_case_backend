from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from src.config import settings

# engine = create_async_engine(settings.database_url_asyncpg)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
#
#
# async def get_async_session():
#     async with async_session_maker() as session:
#         yield session

engine = create_engine(url=settings.database_url_psycopg, echo=False,)
session_maker = sessionmaker(engine)


class Base(DeclarativeBase):
    def dict(self):
        fields_dict = self.__dict__.copy()
        fields_dict.pop('_sa_instance_state')
        return fields_dict
