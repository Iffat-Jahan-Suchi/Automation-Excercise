from Locators.signup_locator import SignupLocators


class SignupPage:

    def __init__(self, page):
        self.page = page
        self.locator = SignupLocators(page)

    def verify_account_information(self):
        self.locator.account_information.wait_for(
            state="visible"
        )

    def fill_account_information(
        self,
        password,
        first_name,
        last_name,
        company,
        address1,
        address2,
        country,
        state,
        city,
        zipcode,
        mobile_number
    ):

        # Title
        self.locator.mr_title.check()

        # Password
        self.locator.password.fill(password)

        # Date of Birth
        self.locator.birth_day.select_option("10")
        self.locator.birth_month.select_option("5")
        self.locator.birth_year.select_option("1998")

        # Newsletter
        self.locator.newsletter.check()

        # Special Offers
        self.locator.special_offers.check()

        # Address Information
        self.locator.first_name.fill(first_name)
        self.locator.last_name.fill(last_name)
        self.locator.company.fill(company)

        self.locator.address1.fill(address1)
        self.locator.address2.fill(address2)

        # Country
        self.locator.country.select_option(
            label=country
        )

        # State
        self.locator.state.fill(state)
        self.locator.city.fill(city)
        self.locator.zipcode.fill(zipcode)
        self.locator.mobile_number.fill(mobile_number)

    def create_account(self):

        self.locator.create_account.scroll_into_view_if_needed()

        self.locator.create_account.click()

    def verify_account_created(self):

        self.locator.account_created.wait_for(
            state="visible"
        )

    def click_continue(self):

        self.locator.continue_button.click()