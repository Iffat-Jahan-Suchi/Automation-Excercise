class RegisterPage:
    def __init__(self,page):
        self.page=page

    def register(self,name,email):
        self.page.locator("//a[normalize-space()='Signup / Login']").click()
        self.page.locator("//input[@placeholder='Name']").fill(name)
        self.page.locator("//input[@data-qa='signup-email']").fill(email)
        self.page.locator("//button[normalize-space()='Signup']").click()


