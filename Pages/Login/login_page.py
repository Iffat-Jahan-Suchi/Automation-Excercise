from Locators.login_locator import LoginLocators


class LoginPage:
    def __init__(self,page):
        self.page=page
        self.locator = LoginLocators(page)

    def credential(self,email,password):
        self.page.locator("//input[@data-qa='login-email']").fill(email)
        self.page.locator("//input[@placeholder='Password']").fill(password)
        self.page.locator("//button[normalize-space()='Login']").click()

    def signup(self, name, email):
        self.locator.signup_name.fill(name)
        self.locator.signup_email.fill(email)
        self.locator.signup_button.click()
