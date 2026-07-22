class AccountInfo:

    def __init__(self, page):
        self.page = page

        # Personal Info
        self.title_mrs = self.page.locator("#id_gender2")
        self.password = self.page.locator("#password")
        self.day = self.page.locator("#days")
        self.month = self.page.locator("#months")
        self.year = self.page.locator("#years")

        self.newsletter = self.page.locator("#newsletter")
        self.offer = self.page.locator("#optin")

        # Address Info
        self.first_name = self.page.locator("#first_name")
        self.last_name = self.page.locator("#last_name")
        self.company = self.page.locator("#company")
        self.address1 = self.page.locator("#address1")
        self.address2 = self.page.locator("#address2")
        self.country = self.page.locator("#country")
        self.state = self.page.locator("#state")
        self.city = self.page.locator("#city")
        self.zipcode = self.page.locator("#zipcode")
        self.mobile = self.page.locator("#mobile_number")

        self.create_account = self.page.locator("button[data-qa='create-account']")

    def register(self,password,first_name,last_name,company,address1,address2,country,state,city,zip,mobile):
        self.title_mrs.check()
        self.page.wait_for_timeout(2000)
        self.page.mouse.wheel(0, 50)

        self.password.fill(password)
        self.page.wait_for_timeout(2000)
        self.page.mouse.wheel(0, 50)

        self.day.select_option("10")
        self.page.wait_for_timeout(2000)

        self.month.select_option("5")
        self.page.wait_for_timeout(2000)

        self.year.select_option("1998")
        self.page.wait_for_timeout(2000)

        self.newsletter.check()
        self.offer.check()
        self.page.wait_for_timeout(2000)
        self.first_name.fill(first_name)
        self.page.wait_for_timeout(2000)

        self.last_name.fill(last_name)
        self.page.wait_for_timeout(2000)
        self.company.fill(company)
        self.page.wait_for_timeout(2000)

        self.address1.fill(address1)
        self.page.wait_for_timeout(2000)

        self.address2.fill(address2)
        self.page.wait_for_timeout(2000)

        self.country.select_option(country)
        self.page.wait_for_timeout(2000)

        self.state.fill(state)
        self.city.fill(city)
        self.zipcode.fill(zip)
        self.mobile.fill(mobile)

        self.page.wait_for_timeout(2000)

        self.create_account.click()