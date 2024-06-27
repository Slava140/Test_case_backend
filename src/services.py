from src.repositories import ProductsRepository, products_repository
from src.schemas import ProductWithID, ProductWithoutID


class ProductsService:
    def __init__(self, repository: ProductsRepository):
        self.repository = repository

    def create_product(self, schema: ProductWithoutID) -> ProductWithID:
        result = self.repository.create(schema.model_dump())
        return ProductWithID(**result)

    def get_product(self, product_id: int) -> ProductWithID:
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"Продукт с ID {product_id} не найден")

        result = self.repository.read(product_id)
        return ProductWithID(**result)

    def get_products(self, page: int, limit: int) -> list[ProductWithID]:
        result = self.repository.read_many(limit=limit, offset=page*limit)

        if not result:
            raise ValueError(f"Продукты не найдены")

        return [ProductWithID(**product) for product in result]

    def update_product(self, product_id: int, schema: ProductWithoutID) -> ProductWithID:
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"Продукт с ID {product_id} не найден")

        result = self.repository.update(product_id, schema.model_dump())
        return ProductWithID(**result)

    def delete_product(self, product_id) -> None:
        if not self.repository.is_id_exists(product_id):
            raise ValueError(f"Продукт с ID {product_id} не найден")

        self.repository.delete(product_id)


products_service = ProductsService(products_repository)