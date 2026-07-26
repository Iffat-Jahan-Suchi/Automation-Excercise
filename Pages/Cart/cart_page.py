from Locators.cart_locator import Cart
from Locators.product_locator import ProductLoc


class CartPage:
    def __init__(self,page):
        self.page=page
        self.locator=Cart(page)

    def verify_first_product(self, name, price):
        assert self.locator.first_product_name.inner_text() == name

        assert self.locator.first_product_price.inner_text() == price

        assert self.locator.first_product_qty.inner_text() == "1"

        assert self.locator.first_total.inner_text() == price

    def verify_second_product(self, name, price):
        assert self.locator.sec_product_name.inner_text() == name

        assert self.locator.sec_product_price.inner_text() == price

        assert self.locator.sec_product_qty.inner_text() == "1"

        assert self.locator.sec_total.inner_text() == price

