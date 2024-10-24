import pytest
from src.main import Product, Category

@pytest.fixture(scope="module")
def sample_product():
    return Product("Sample Phone", "Description", 1000.0, 10)

@pytest.fixture(scope="module")
def sample_category():
    return Category("Sample Category", "Description", [])

@pytest.fixture(scope="function")
def reset_product_count():
    original_count = Category.product_count
    yield
    Category.product_count = original_count
