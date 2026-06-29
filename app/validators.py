def validate_name(name):
    if not isinstance(name, str):
        return "Название товара должно быть строкой"

    if name.strip() == "":
        return "Название товара не может быть пустым"

    return None


def validate_price(price):
    if not isinstance(price, int) and not isinstance(price, float):
        return "Цена должна быть числом"

    if price <= 0:
        return "Цена должна быть больше 0"

    return None


def validate_quantity(quantity):
    if not isinstance(quantity, int):
        return "Количество должно быть целым числом"

    if quantity < 0:
        return "Количество не может быть меньше 0"

    return None


def validate_product_data(name, price, quantity):
    name_error = validate_name(name)
    if name_error is not None:
        return name_error

    price_error = validate_price(price)
    if price_error is not None:
        return price_error

    quantity_error = validate_quantity(quantity)
    if quantity_error is not None:
        return quantity_error

    return None