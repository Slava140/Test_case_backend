import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from database import Base, engine
from routers import products_router

Base.metadata.create_all(bind=engine)
app = FastAPI(openapi_url="/core/openapi.json", docs_url="/core/docs")
app.include_router(products_router)


@app.get("/")
def main():
    return "Главная страница"


if __name__ == '__main__':
    uvicorn.run("app:app")
