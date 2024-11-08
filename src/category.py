from itertools import product

from src.product import Product


class Category:
    """Класс для представления категории"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод инициализации класса категории"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Метод строкового отображения имя категории, количество товаров"""
        products_in_stock = 0
        for product in self.__products:
            products_in_stock += product.quantity
        return f"{self.name}, количество продуктов: {products_in_stock} шт."

    def add_product(self, product: Product = None):
        """Специальный метод добавления объекта класса в приватный атрибут,
        через проверку принадлежности родительскому классу isinstance"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        """Метод возвращает строку с названием продукта, стоимость и остаток"""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str

    @property
    def list_product(self):
        """Подсчитывает средний ценник всех товаров."""
        return self.__products

    def middle_price(self):
        try:
            return sum([product.price for product in self.__products]) / len(
                self.__products
            )
        except ZeroDivisionError:
            return 0
