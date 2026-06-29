from app.services import ProductService
from app.storage import reset_products


def print_response(title, response):
    print(f"\n=== {title} ===")

    if response["success"]:
        print("Успех:")
        print(response["data"])
    else:
        print("Ошибка:")
        print(response["error"])


def main():
    reset_products()

    service = ProductService()

    print_response(
        "Список товаров",
        service.get_all_products()
    )

    print_response(
        "Создание товара",
        service.create_product("Keyboard", 3500, 4)
    )

    print_response(
        "Создание товара с некорректной ценой",
        service.create_product("Monitor", -100, 2)
    )

    print_response(
        "Поиск товара по id",
        service.get_product_response(1)
    )

    print_response(
        "Поиск несуществующего товара",
        service.get_product_response(100)
    )

    print_response(
        "Доступные товары",
        service.get_available_products()
    )

    print_response(
        "Обновление товара",
        service.update_product(1, "TV Pro", 45000, 2)
    )

    print_response(
        "Удаление товара",
        service.delete_product(2)
    )

    print_response(
        "Итоговый список товаров",
        service.get_all_products()
    )


if __name__ == "__main__":
    main()