from playwright.sync_api import Page


class CheckoutLocators:

    def __init__(self, page: Page):
        self.page = page

        # Address
        self.address_details = page.get_by_text(
            "Address Details", exact=True
        )

        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")

        # Review order
        self.review_order = page.get_by_text(
            "Review Your Order", exact=True
        )

        # Comment
        self.order_comment = page.locator(
            'textarea[name="message"]'
        )

        # Place order
        self.place_order = page.get_by_text(
            "Place Order", exact=True
        )