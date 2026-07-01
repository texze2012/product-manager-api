from dbm import error
from http.client import HTTPException

from fastapi import FastAPI, HTTPException, status
from app.schemas import ProductCreateRequest, ProductUpdateRequest
from app.services import ProductService

app = FastAPI(
    title="Product Manager API",
    description="Учебный backend API для управления товарами",
    version="1.0.0",
)

service = ProductService()

def handle_response(response):
    if response["success"]:
        return response

    error = response["error"]

    if error == "Товар не найден":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=error
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=error
    )
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
    response = service.get_product_response(product_id)
    return handle_response(response)

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreateRequest):
    response = service.create_product(
        product.name,
        product.price,
        product.quantity
    )

    return handle_response(response)

@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdateRequest):
    response = service.update_product(
        product_id,
        product.name,
        product.price,
        product.quantity
    )

    return handle_response(response)

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    response = service.delete_product(product_id)
    return handle_response(response)