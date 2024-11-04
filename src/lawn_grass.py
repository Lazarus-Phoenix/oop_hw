from src.product import Product


class LawnGrass(Product):
    """ Дочерний Класс и конструктор к категории продукта трава гозонная"""
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод сложения всей стоимости всего товара этой категории на складе"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
    