from Pages.Products.all_products import Products


def test_products(page):
    products=Products(page)
    products.all_product()

