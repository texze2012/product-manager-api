from fastapi import FastAPI
from pydantic import BaseModel

from app.services import ProductService

app = FastAPI(
    title="Product Manager API",
    description="Учебный backend API для управления товарами",
    version="1.0.0",
)

service = ProductService()

class ProductCreateRequest(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdateRequest(BaseModel):
    name: str
    price: float
    quantity: int
@app.get("/")
def root():
    return {
        "message": "Product Manager API запущен",
    }

@app.get("/products")
def get_products():
    return service.get_all_products()

@app.get("/products/available")
def get_available_products():
    return service.get_available_products()

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return service.get_product_response(product_id)

@app.post("/products")
def create_product(product: ProductCreateRequest):
    return service.create_product(
        product.name,
        product.price,
        product.quantity,
    )

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdateRequest):
    return service.update_product(
        product_id,
        product.name,
        product.price,
        product.quantity
    )

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    return service.delete_product(product_id)
