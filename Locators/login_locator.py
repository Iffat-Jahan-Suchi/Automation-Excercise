from playwright.sync_api import Page


class LoginLocators:

    def __init__(self, page: Page):
        self.page = page

        # New User Signup section
        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"]')

        self.signup_button = page.locator(
            '[data-qa="signup-button"]'
        )

        # Login page heading
        self.login_page = page.get_by_text(
            "Login to your account", exact=True
        )