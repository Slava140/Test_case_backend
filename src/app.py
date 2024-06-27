from fastapi import FastAPI

from src.database import Base, engine
from src.routers import products_router


Base.metadata.create_all(bind=engine)
app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")
app.include_router(products_router)


@app.get("/")
def main():
    return "Главная страница"
