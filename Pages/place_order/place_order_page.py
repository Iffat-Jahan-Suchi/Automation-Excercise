from Locators.place_order_locator import PlaceOrderLoc


class PlaceOrderPage:

    def __init__(self, page):
        self.page = page
        self.locator = PlaceOrderLoc(page)

    # ==================================================
    # PRODUCTS
    # ==================================================

    def add_products_to_cart(self):

        # First Product
        self.locator.first_product.hover()

        self.locator.first_product.locator(
            "a.add-to-cart"
        ).click()

        # Continue Shopping
        self.locator.continue_shopping.click()

        # Second Product
        self.locator.second_product.hover()

        self.locator.second_product.locator(
            "a.add-to-cart"
        ).click()

    # ==================================================
    # CART
    # ==================================================

    def open_cart(self):

        # Header Cart
        self.locator.cart.click()

    def verify_cart_page(self):

        self.locator.shopping_cart.wait_for(
            state="visible"
        )

        assert self.locator.shopping_cart.is_visible()

    def proceed_to_checkout(self):

        self.locator.proceed_to_checkout.click()

    # ==================================================
    # REGISTER / LOGIN
    # ==================================================

    def click_register_login(self):

        self.locator.register_login.click()

    # ==================================================
    # SIGNUP
    # ==================================================

    def signup(self, name, email):

        self.locator.signup_name.fill(name)

        self.locator.signup_email.fill(email)

        self.locator.signup_button.click()

    # ==================================================
    # ACCOUNT INFORMATION
    # ==================================================

    def fill_account_information(self):

        # Title
        self.locator.mr.check()

        # Password
        self.locator.password.fill(
            "Test@12345"
        )

        # Date of Birth
        self.locator.days.select_option(
            "10"
        )

        self.locator.months.select_option(
            "5"
        )

        self.locator.years.select_option(
            "1998"
        )

        # Newsletter
        self.locator.newsletter.check()

        # Special Offers
        self.locator.optin.check()

        # Personal Information
        self.locator.first_name.fill(
            "Iffat"
        )

        self.locator.last_name.fill(
            "Jahan"
        )

        self.locator.company.fill(
            "Test Company"
        )

        # Address
        self.locator.address1.fill(
            "Dhaka, Bangladesh"
        )

        self.locator.address2.fill(
            "Mirpur"
        )

        # Country
        self.locator.country.select_option(
            label="India"
        )

        self.locator.state.fill(
            "Dhaka"
        )

        self.locator.city.fill(
            "Dhaka"
        )

        self.locator.zipcode.fill(
            "1207"
        )

        self.locator.mobile_number.fill(
            "01712345678"
        )

    # ==================================================
    # CREATE ACCOUNT
    # ==================================================

    def create_account(self):

        self.locator.create_account.click()

        # Wait until account-created page loads
        self.page.wait_for_url(
            "**/account_created",
            timeout=30000
        )

    def verify_account_created(self):

        self.locator.account_created.wait_for(
            state="visible",
            timeout=30000
        )

        assert self.locator.account_created.is_visible()

    # ==================================================
    # CONTINUE
    # ==================================================

    def click_continue(self):

        self.locator.continue_button.click()

    # ==================================================
    # LOGIN VERIFICATION
    # ==================================================

    def verify_logged_in(self):

        self.locator.logged_in_as.wait_for(
            state="visible"
        )

        assert self.locator.logged_in_as.is_visible()

    # ==================================================
    # CHECKOUT
    # ==================================================

    def verify_checkout_page(self):

        self.locator.address_details.wait_for(
            state="visible"
        )

        self.locator.review_order.wait_for(
            state="visible"
        )

        assert self.locator.address_details.is_visible()

        assert self.locator.review_order.is_visible()

    def enter_order_comment(self, comment):

        self.locator.comment.fill(
            comment
        )

    def click_place_order(self):

        self.locator.place_order.click()

    # ==================================================
    # PAYMENT
    # ==================================================

    def enter_payment_details(self):

        self.locator.name_on_card.fill(
            "Iffat Jahan"
        )

        self.locator.card_number.fill(
            "4111111111111111"
        )

        self.locator.cvc.fill(
            "123"
        )

        self.locator.expiry_month.fill(
            "12"
        )

        self.locator.expiry_year.fill(
            "2030"
        )

    def pay_and_confirm_order(self):

        self.locator.pay_and_confirm.click()

    # ==================================================
    # ORDER SUCCESS
    # ==================================================

    def verify_order_success(self):

        self.locator.order_success.wait_for(
            state="visible",
            timeout=30000
        )

        assert self.locator.order_success.is_visible()

    # ==================================================
    # DELETE ACCOUNT
    # ==================================================

    def delete_account(self):

        self.locator.delete_account.click()

    def verify_account_deleted(self):

        self.locator.account_deleted.wait_for(
            state="visible",
            timeout=30000
        )

        assert self.locator.account_deleted.is_visible()