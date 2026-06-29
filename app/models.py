class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_available = quantity > 0

    def update(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.is_available = quantity > 0

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "is_available": self.is_available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["price"],
            data["quantity"]
        )