import unittest
import io
import sys
from src.product import Product


class TestProduct(unittest.TestCase):

    def test_init(self):
        product = Product("Товар", "Описание товара", 100, 50)
        self.assertEqual(product.name, "Товар")
        self.assertEqual(product.description, "Описание товара")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 50)

    def test_new_product(self):
        existing_product = Product("Старый товар", "Описание старого товара", 100, 50)
        new_product_dict = {"name": "Новый товар", "description": "Описание нового товара", "price": 200,
                            "quantity": 30}
        new_product = Product.new_product(new_product_dict, products=[existing_product])
        self.assertEqual(new_product.name, "Новый товар")
        self.assertEqual(new_product.description, "Описание нового товара")
        self.assertEqual(new_product.price, 200)
        self.assertEqual(new_product.quantity, 30)

    def test_price_getter(self):
        product = Product("Товар", "", 100, 0)
        self.assertEqual(product.price, 100)

    def test_price_setter_positive(self):
        product = Product("Товар", "", 100, 0)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        product.new_price = 150
        sys.stdout = sys.__stdout__
        self.assertEqual(product.new_price, 150)
        self.assertNotIn("Цена не должна быть нулевая или отрицательная", capturedOutput.getvalue().strip())

    def test_price_setter_negative(self):
        product = Product("Товар", "", 100, 0)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        product.price = -50
        sys.stdout = sys.__stdout__
        self.assertEqual(product.price, 100)
        self.assertIn("Цена не должна быть нулевая или отрицательная", capturedOutput.getvalue().strip())

    def test_price_setter_zero(self):
        product = Product("Товар", "", 100, 0)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        product.price = 0
        sys.stdout = sys.__stdout__
        self.assertEqual(product.price, 100)
        self.assertIn("Цена не должна быть нулевая или отрицательная", capturedOutput.getvalue().strip())




if __name__ == '__main__':
    unittest.main()