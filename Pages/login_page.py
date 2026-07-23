class LoginPage:
    def __init__(self,page):
        self.page=page

    def credential(self,email,password):
        self.page.locator("//input[@data-qa='login-email']").fill(email)
        self.page.locator("//input[@placeholder='Password']").fill(password)
        self.page.locator("//button[normalize-space()='Login']").click()
