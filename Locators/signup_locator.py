from playwright.sync_api import Page


class SignupLocators:

    def __init__(self, page: Page):
        self.page = page

        # Account Information
        self.account_information = page.locator(
            "h2.title"
        ).filter(
            has_text="Enter Account Information"
        )

        # Title
        self.mr_title = page.locator("#id_gender1")
        self.mrs_title = page.locator("#id_gender2")

        # Password
        self.password = page.locator(
            '[data-qa="password"]'
        )

        # Date of Birth
        self.birth_day = page.locator(
            '[data-qa="days"]'
        )

        self.birth_month = page.locator(
            '[data-qa="months"]'
        )

        self.birth_year = page.locator(
            '[data-qa="years"]'
        )

        # Newsletter
        self.newsletter = page.locator(
            "#newsletter"
        )

        # Special Offers
        self.special_offers = page.locator(
            "#optin"
        )

        # Address Information
        self.first_name = page.locator(
            '[data-qa="first_name"]'
        )

        self.last_name = page.locator(
            '[data-qa="last_name"]'
        )

        self.company = page.locator(
            '[data-qa="company"]'
        )

        self.address1 = page.locator(
            '[data-qa="address"]'
        )

        self.address2 = page.locator(
            '[data-qa="address2"]'
        )

        self.country = page.locator(
            '[data-qa="country"]'
        )

        self.state = page.locator(
            '[data-qa="state"]'
        )

        self.city = page.locator(
            '[data-qa="city"]'
        )

        self.zipcode = page.locator(
            '[data-qa="zipcode"]'
        )

        self.mobile_number = page.locator(
            '[data-qa="mobile_number"]'
        )

        # Create Account
        self.create_account = page.locator(
            '[data-qa="create-account"]'
        )

        # Account Created
        self.account_created = page.get_by_text(
            "ACCOUNT CREATED!",
            exact=False
        )

        # Continue
        self.continue_button = page.get_by_text(
            "Continue",
            exact=True
        )