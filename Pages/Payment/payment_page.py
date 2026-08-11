from Locators.payment_locator import PaymentLocators


class PaymentPage:

    def __init__(self, page):
        self.page = page
        self.locator = PaymentLocators(page)

    # --------------------------------------------------
    # Enter Payment Details
    # --------------------------------------------------

    def enter_payment_details(
        self,
        name_on_card,
        card_number,
        cvc,
        expiry_month,
        expiry_year
    ):

        self.locator.name_on_card.fill(
            name_on_card
        )

        self.locator.card_number.fill(
            card_number
        )

        self.locator.cvc.fill(
            cvc
        )

        self.locator.expiry_month.fill(
            expiry_month
        )

        self.locator.expiry_year.fill(
            expiry_year
        )

    # --------------------------------------------------
    # Pay and Confirm Order
    # --------------------------------------------------

    def pay_and_confirm_order(self):

        self.locator.pay_and_confirm_order.click()

    # --------------------------------------------------
    # Verify Order Success
    # --------------------------------------------------

    def verify_order_success(self):

        self.locator.order_success.wait_for(
            state="visible"
        )

    # --------------------------------------------------
    # Delete Account
    # --------------------------------------------------

    def delete_account(self):

        self.locator.delete_account.click()

    # --------------------------------------------------
    # Verify Account Deleted
    # --------------------------------------------------

    def verify_account_deleted(self):

        self.locator.account_deleted.wait_for(
            state="visible"
        )

    # --------------------------------------------------
    # Continue
    # --------------------------------------------------

    def click_continue(self):

        self.locator.continue_button.click()

