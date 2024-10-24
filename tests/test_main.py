import pytest
from src.main import Product, Category


def test_product_init():
    product = Product("Test Phone", "Description", 1000.0, 10)
    assert product.name == "Test Phone"
    assert product.description == "Description"
    assert pytest.approx(product.price, abs=0.01) == 1000.0
    assert product.quantity == 10
    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)


def test_category_init():
    category = Category("Sample Category", "Description", [])
    assert category.name == "Sample Category"
    assert category.description == "Description"
    assert len(category.products) == 0
    assert category.category_count == 1
    assert category.product_count == 0


def test_category_add_product():
    category = Category("Sample Category", "Description", [])
    product = Product("Test Phone", "Description", 1000.0, 10)
    category.products.append(product)

    assert len(category.products) == 1
    assert category.products[0].name == "Test Phone"
    assert category.category_count == 2
    assert category.product_count == 0



def test_category_class_variables():
    assert Category.category_count == 2
    assert Category.product_count == 0

    category1 = Category("Category 1", "Desc 1", [])
    category2 = Category("Category 2", "Desc 2", [])

    assert Category.category_count == 4
    assert Category.product_count == 0

    category1.products.append(Product("Product 1", "Desc 1", 100.0, 5))
    category2.products.append(Product("Product 2", "Desc 2", 200.0, 3))

    assert Category.category_count == 4
    assert Category.product_count == 0
