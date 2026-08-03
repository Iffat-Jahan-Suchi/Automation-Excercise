import time

from Pages.Register.account_info import AccountInfo
from Pages.Register.register_page import RegisterPage
from conftest import page

def test_register(page):
    my_register = RegisterPage(page)
    email = f"iffat{int(time.time())}@gmail.com"

    my_register.register(
        "jahan",
        email
    )
    page.wait_for_timeout(2000)
    my_ac_info = AccountInfo(page)
    my_ac_info.register(
        password="123456",
        first_name="Iffat",
        last_name="Jahan",
        company="ABC Ltd",
        address1="Dhaka",
        address2="Mirpur",
        country="India",
        state="Dhaka",
        city="Dhaka",
        zip="1216",
        mobile="01712345678"
    )
    assert page.url == "https://automationexercise.com/account_created"
    page.locator("//a[@class='btn btn-primary']").click()
    page.wait_for_timeout(3000)
    assert page.locator("text=Logged in as jahan").is_visible()
    page.locator("a[href='/delete_account']").click()

def test_register_existing_mail(page):
    existing_mail_reg = RegisterPage(page)
    existing_mail_reg.register("jahan","ij@gmail.com")
    assert page.locator("text=Email Address already exist!").is_visible()






