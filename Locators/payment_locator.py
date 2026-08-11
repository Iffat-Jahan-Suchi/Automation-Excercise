from playwright.sync_api import Page


class PaymentLocators:

    def __init__(self, page: Page):
        self.page = page

        # Payment fields
        self.name_on_card = page.locator(
            '[data-qa="name-on-card"]'
        )

        self.card_number = page.locator(
            '[data-qa="card-number"]'
        )

        self.cvc = page.locator(
            '[data-qa="cvc"]'
        )

        self.expiry_month = page.locator(
            '[data-qa="expiry-month"]'
        )

        self.expiry_year = page.locator(
            '[data-qa="expiry-year"]'
        )

        # Pay and Confirm Order
        self.pay_and_confirm_order = page.locator(
            '[data-qa="pay-button"]'
        )

        # Order success
        # Automation Exercise displays "Order Placed!"
        self.order_success = page.get_by_text(
            "Order Placed!",
            exact=True
        )

        # Delete Account
        self.delete_account = page.get_by_text(
            "Delete Account",
            exact=True
        )

        # Account Deleted
        self.account_deleted = page.get_by_text(
            "ACCOUNT DELETED!",
            exact=False
        )

        # Continue
        self.continue_button = page.get_by_text(
            "Continue",
            exact=True
        )

