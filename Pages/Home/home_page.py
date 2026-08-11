from Locators.home_locator import HomeLocators


class HomePage:

    def __init__(self, page):
        self.page = page
        self.locator = HomeLocators(page)

    def verify_home_page(self):
        self.locator.home_page.wait_for()

    def add_products_to_cart(self):

        # Go to Products
        self.locator.products_button.click()

        # First product
        self.locator.first_product.hover()
        self.locator.first_add_to_cart.click()

        # Continue shopping
        self.locator.continue_shopping.click()

        # Second product
        self.locator.second_product.hover()
        self.locator.second_add_to_cart.click()

    def click_cart(self):
        self.locator.cart_button.click()