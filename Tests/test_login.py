from Pages.Login.login_page import LoginPage

def test_valid_login(page):
    page.locator("//a[normalize-space()='Signup / Login']").click()
    assert page.locator("text=Login to your account").is_visible()
    page.wait_for_timeout(3000)
    login=LoginPage(page)
    login.credential("ij@gmail.com","123456")
    assert page.locator("text=Logout").is_visible()


def test_invalid_login(page):
    page.locator("//a[normalize-space()='Signup / Login']").click()
    assert page.locator("text=Login to your account").is_visible()
    page.wait_for_timeout(3000)
    login=LoginPage(page)
    login.credential("ij@gmail.com","1234")
    assert page.locator("text=Your email or password is incorrect!").is_visible()

def test_logout(page):
    page.locator("//a[normalize-space()='Signup / Login']").click()
    assert page.locator("text=Login to your account").is_visible()
    page.wait_for_timeout(3000)
    login=LoginPage(page)
    login.credential("ij@gmail.com","123456")
    assert page.locator("text=Logged in as jahan").is_visible()
    assert page.locator("text=Logout").is_visible()
    page.wait_for_timeout(2000)
    page.locator("//a[normalize-space()='Logout']").click()
    page.wait_for_timeout(2000)
    assert page.url=="https://automationexercise.com/login"