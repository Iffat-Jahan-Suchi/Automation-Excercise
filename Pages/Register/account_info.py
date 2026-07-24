from Locators.personal_info import PersonalInfo
class AccountInfo:

    def __init__(self, page):
        self.page = page
        self.locator=PersonalInfo(page)

    def register(
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
            zip,
            mobile
    ):
        self.locator.title_mrs.check()
        self.locator.password.fill(password)

        self.locator.day.select_option("10")
        self.locator.month.select_option("5")
        self.locator.year.select_option("1998")

        self.locator.newsletter.check()
        self.locator.offer.check()

        self.locator.first_name.fill(first_name)
        self.locator.last_name.fill(last_name)
        self.locator.company.fill(company)
        self.locator.address1.fill(address1)
        self.locator.address2.fill(address2)

        self.locator.country.select_option(country)
        self.locator.state.fill(state)
        self.locator.city.fill(city)
        self.locator.zipcode.fill(zip)
        self.locator.mobile.fill(mobile)

        self.locator.create_account.click()

