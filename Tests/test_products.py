from Pages.Cart.cart_page import CartPage
from Pages.Products.add_product import AddProducts
from Pages.Products.all_products import Products


def test_detail_products(page):
    products=Products(page)
    products.all_product()

def test_add_to_cart(page):
    addToCart=AddProducts(page)
    CartList=CartPage(page)
    first_name, first_price = addToCart.add_first_product()
    second_name, second_price = addToCart.add_second_product()
    CartList.verify_first_product(first_name, first_price)
    CartList.verify_second_product(second_name, second_price)


