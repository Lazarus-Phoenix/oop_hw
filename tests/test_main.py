import pytest
from src.category import Category
from src.product import Product



@pytest.fixture
def sample_category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )

def test_category_creation(sample_category):
    assert isinstance(sample_category, Category)
    assert len(sample_category.products) == 146
    assert sample_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"

def test_adding_product_to_category(sample_category):
    new_product = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    sample_category.add_product(new_product)
    assert len(sample_category.products) == 188
    assert 'in <string>'

def test_product_creation_and_properties():
    product = Product("Test Phone", "Test description", 9999.99, 10)
    assert product.name == "Test Phone"
    assert product.description == "Test description"
    assert product.price == 9999.99
    assert product.quantity == 10


def test_new_product_creation():
    new_product_data = {"name": "Test Phone", "description": "Test description", "price": 9999.99, "quantity": 10}
    new_product = Product.new_product(new_product_data)
    assert isinstance(new_product, Product)
    assert new_product.name == "Test Phone"
    assert new_product.description == "Test description"
    assert new_product.price == 9999.99
    assert new_product.quantity == 10