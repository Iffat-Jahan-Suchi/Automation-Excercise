class PersonalInfo:
    def __init__(self,page):
        self.page=page

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