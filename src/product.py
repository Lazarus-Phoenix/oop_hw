from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления продукта"""

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации класса продукта. Задаем значения атрибутам"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()  # Инициализатор родительского класса Mixin

    def __str__(self):
        """Метод строковое отображение названия, цены, остатка на складе"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод сложения всей стоимости всего товара на складе"""
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, dict_product, products=None):
        """Метод добавляет новый продукт"""
        if products:
            for product in products:
                if product.name == dict_product["name"]:
                    product.description = dict_product["description"]
                    product.quantity += dict_product["quantity"]
                    product.price = max([product.price, dict_product["price"]])
                    return product
        return cls(**dict_product)

    @property
    def price(self):
        """Метод возвращает цену продукта"""
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            check_input = input("Изменять цену? Введите y если да, и n если нет.\n")
            if check_input != "y":
                return
            self.__price = new_price
