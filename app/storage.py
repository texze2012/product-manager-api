import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "products.json"


DEFAULT_PRODUCTS = [
    {
        "id": 1,
        "name": "TV",
        "price": 30000,
        "quantity": 6,
        "is_available": True
    },
    {
        "id": 2,
        "name": "Laptop",
        "price": 50000,
        "quantity": 2,
        "is_available": True
    },
    {
        "id": 3,
        "name": "Mouse",
        "price": 1500,
        "quantity": 0,
        "is_available": False
    }
]


def load_products():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_products(products):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)


def reset_products():
    save_products(DEFAULT_PRODUCTS)