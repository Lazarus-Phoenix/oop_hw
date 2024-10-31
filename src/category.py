from src.product import Product


class Category:
    """Класс для представления категории"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод инициализации класса категории. Задаем значения атрибутам экземпляра"""
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
        return f'{self.name}, количество продуктов: {products_in_stock} шт.'

    def add_product(self, product: Product = None):
        """Специальный метод передачи объекта класса в приватный атрибут"""
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
