from Locators.checkout_locator import CheckoutLocators


class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self.locator = CheckoutLocators(page)

    def verify_checkout_page(self):

        self.locator.address_details.wait_for()

        self.locator.delivery_address.wait_for()

        self.locator.billing_address.wait_for()

        self.locator.review_order.wait_for()

    def enter_comment(self, comment):
        self.locator.order_comment.fill(comment)

    def place_order(self):
        self.locator.place_order.click()