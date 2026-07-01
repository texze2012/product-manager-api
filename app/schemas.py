from pydantic import BaseModel

class ProductCreateRequest(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdateRequest(BaseModel):
    name: str
    price: float
    quantity: int