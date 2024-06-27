from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse, Response

from services import products_service
from schemas import ProductWithoutID

products_router = APIRouter(prefix="/products", tags=["products"])


@products_router.post('/')
def create_product(product_schema: ProductWithoutID) -> JSONResponse:
    try:
        return JSONResponse(
            status_code=201,
            content=products_service.create_product(product_schema).model_dump()
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='При выполнении операции произошла неизвестная ошибка'
        )


@products_router.get('/{product_id}')
def read_product(product_id: int) -> JSONResponse:
    try:
        return JSONResponse(
            status_code=200,
            content=products_service.get_product(product_id).model_dump()
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='При выполнении операции произошла неизвестная ошибка'
        )


@products_router.get('/')
def read_products(page: int = 0, limit: int = 5):
    try:
        products = products_service.get_products(page=page, limit=limit)
        product_jsons = [product.model_dump() for product in products]
        return JSONResponse(
            status_code=200,
            content=product_jsons
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='При выполнении операции произошла неизвестная ошибка'
        )


@products_router.put('/{product_id}')
def update_product(product_id: int, schema: ProductWithoutID):
    try:
        return JSONResponse(
            status_code=200,
            content=products_service.update_product(product_id, schema).model_dump()
        )
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='При выполнении операции произошла неизвестная ошибка'
        )


@products_router.delete('/{product_id}')
def delete_product(product_id: int) -> Response:
    try:
        products_service.delete_product(product_id)
        return Response(status_code=202)
    except ValueError as error:
        raise HTTPException(
            status_code=404,
            detail=str(error)
        )
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail='При выполнении операции произошла неизвестная ошибка'
        )

