from app.models import Product
from app.responses import success_response, error_response
from app.storage import load_products, save_products
from app.validators import validate_product_data


class ProductService:
    def __init__(self):
        self.products = self.load_products_from_storage()

    def load_products_from_storage(self):
        products_data = load_products()

        products = []

        for product_data in products_data:
            products.append(Product.from_dict(product_data))

        return products

    def save(self):
        products_data = []

        for product in self.products:
            products_data.append(product.to_dict())

        save_products(products_data)

    def get_all_products(self):
        products_data = []

        for product in self.products:
            products_data.append(product.to_dict())

        return success_response(products_data)

    def get_available_products(self):
        available_products = []

        for product in self.products:
            if product.is_available:
                available_products.append(product.to_dict())

        return success_response(available_products)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product

        return None

    def get_product_response(self, product_id):
        product = self.get_product_by_id(product_id)

        if product is None:
            return error_response("Товар не найден")

        return success_response(product.to_dict())

    def get_next_product_id(self):
        max_product_id = 0

        for product in self.products:
            if product.id > max_product_id:
                max_product_id = product.id

        return max_product_id + 1

    def create_product(self, name, price, quantity):
        validation_error = validate_product_data(name, price, quantity)

        if validation_error is not None:
            return error_response(validation_error)

        product = Product(
            self.get_next_product_id(),
            name,
            price,
            quantity
        )

        self.products.append(product)
        self.save()

        return success_response(product.to_dict())

    def update_product(self, product_id, name, price, quantity):
        product = self.get_product_by_id(product_id)

        if product is None:
            return error_response("Товар не найден")

        validation_error = validate_product_data(name, price, quantity)

        if validation_error is not None:
            return error_response(validation_error)

        product.update(name, price, quantity)
        self.save()

        return success_response(product.to_dict())

    def delete_product(self, product_id):
        product = self.get_product_by_id(product_id)

        if product is None:
            return error_response("Товар не найден")

        self.products.remove(product)
        self.save()

        return success_response(product.to_dict())