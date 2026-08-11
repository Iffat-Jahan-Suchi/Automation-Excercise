class Cart:
    def __init__(self,page):
        self.page=page

        #First product info
        self.first_product_name=self.page.locator(".cart_description a").nth(0)
        self.first_product_price=self.page.locator(".cart_price p").nth(0)
        self.first_product_qty=self.page.locator(".cart_quantity button").nth(0)
        self.first_total = page.locator(".cart_total p").nth(0)

        # Second product info
        self.sec_product_name = self.page.locator(".cart_description a").nth(1)
        self.sec_product_price = self.page.locator(".cart_price p").nth(1)
        self.sec_product_qty = self.page.locator(".cart_quantity button").nth(1)
        self.sec_total = page.locator(".cart_total p").nth(1)
        self.cart_qty=page.locator(".cart_quantity button")

        self.cart_page = page.locator("#cart_info")

        # Proceed to checkout
        self.proceed_to_checkout = page.get_by_text(
            "Proceed To Checkout", exact=True
        )

        # Register / Login button
        self.register_login = page.get_by_text(
            "Register / Login", exact=True
        )



