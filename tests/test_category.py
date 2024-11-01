import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def category():
    return Category("Electronics", "Electronic devices", [])

@pytest.fixture
def product():
    return Product("Laptop", "", 1000, 50)

def test_category_creation(category):
    assert category.name == "Electronics"
    assert category.description == "Electronic devices"
    assert category.products == ''

def test_add_product_to_category(category, product):
    category.add_product(product)
    assert len(category.products) == 34
    assert category.products[0] == "L"

def test_category_count_increments(category):
    initial_count = Category.category_count
    category = Category("Electronics", "Electronic devices", [])
    assert Category.category_count == initial_count + 1

def test_product_count_increments(category, product):
    initial_count = Category.product_count
    category.add_product(product)
    assert Category.product_count == initial_count + 1

def test_products_property_returns_string(category, product):
    category.add_product(product)
    expected_output = (
        "Laptop, 1000 руб. Остаток: 50 шт.\n"
    )
    assert category.products == expected_output

def test_add_product_with_non_product_raises_error(category):
    with pytest.raises(TypeError):
        category.add_product("Not a product")

# Дополнительный тест для класса Product
def test_product_creation():
    product = Product("Test Product", "", 99, 100)
    assert product.name == "Test Product"
    assert product.price == 99
    assert product.quantity == 100

def test_category_str(category):
    assert str(category) == 'Electronics, количество продуктов: 0 шт.'
