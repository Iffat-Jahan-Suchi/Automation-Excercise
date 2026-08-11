from playwright.sync_api import Page


class HomeLocators:

    def __init__(self, page: Page):
        self.page = page

        # Home
        self.home_page = page.locator("body")

        # Products
        self.products_button = page.locator(
            'a[href="/products"]'
        )

        # First product
        self.first_product = page.locator(
            ".productinfo"
        ).nth(0)

        self.first_add_to_cart = self.first_product.get_by_text(
            "Add to cart",
            exact=True
        )

        # Second product
        self.second_product = page.locator(
            ".productinfo"
        ).nth(1)

        self.second_add_to_cart = self.second_product.get_by_text(
            "Add to cart",
            exact=True
        )

        # Continue Shopping popup button
        self.continue_shopping = page.get_by_text(
            "Continue Shopping",
            exact=True
        )

        # Popup View Cart
        self.view_cart_popup = page.get_by_text(
            "View Cart",
            exact=True
        )

        # Navbar Cart
        self.cart_button = page.locator(
            'a[href="/view_cart"]'
        ).first