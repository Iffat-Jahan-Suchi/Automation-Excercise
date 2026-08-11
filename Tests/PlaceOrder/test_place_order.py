import time

from Pages.Home.home_page import HomePage
from Pages.Cart.cart_page import CartPage
from Pages.Login.login_page import LoginPage
from Pages.SignUp.signup_page import SignupPage
from Pages.Checkout.checkout_page import CheckoutPage
from Pages.Payment.payment_page import PaymentPage


def test_place_order_register_while_checkout(page):

    # --------------------------------------------------
    # Test Data
    # --------------------------------------------------

    name = "Iffat Jahan"

    # Unique email for every test run
    email = f"iffat{int(time.time())}@gmail.com"

    password = "Test@12345"

    first_name = "Iffat"
    last_name = "Jahan"
    company = "Test Company"
    address1 = "Dhaka"
    address2 = "Mirpur"
    country = "India"
    state = "Dhaka"
    city = "Dhaka"
    zipcode = "1216"
    mobile_number = "01712345678"

    comment = "Please deliver my order carefully."

    card_name = "Iffat Jahan"
    card_number = "4111111111111111"
    cvc = "123"
    expiry_month = "12"
    expiry_year = "2030"

    # --------------------------------------------------
    # Page Objects
    # --------------------------------------------------

    home = HomePage(page)
    cart = CartPage(page)
    login = LoginPage(page)
    signup = SignupPage(page)
    checkout = CheckoutPage(page)
    payment = PaymentPage(page)

    # --------------------------------------------------
    # 1. Launch browser
    # --------------------------------------------------
    # Browser is handled by conftest.py

    # --------------------------------------------------
    # 2. Navigate to URL
    # --------------------------------------------------

    page.goto("https://automationexercise.com/")

    # --------------------------------------------------
    # 3. Verify Home Page
    # --------------------------------------------------

    home.verify_home_page()

    # --------------------------------------------------
    # 4. Add products to cart
    # --------------------------------------------------

    home.add_products_to_cart()

    # --------------------------------------------------
    # 5. Click Cart
    # --------------------------------------------------

    home.click_cart()

    # --------------------------------------------------
    # 6. Verify Cart Page
    # --------------------------------------------------

    cart.verify_cart_page()

    # --------------------------------------------------
    # 7. Click Proceed To Checkout
    # --------------------------------------------------

    cart.proceed_to_checkout()

    # --------------------------------------------------
    # 8. Click Register / Login
    # --------------------------------------------------

    cart.click_register_login()

    # --------------------------------------------------
    # 9. Register New User
    # --------------------------------------------------

    login.signup(
        name=name,
        email=email
    )

    # --------------------------------------------------
    # Account Information
    # --------------------------------------------------

    signup.verify_account_information()

    signup.fill_account_information(
        password=password,
        first_name=first_name,
        last_name=last_name,
        company=company,
        address1=address1,
        address2=address2,
        country=country,
        state=state,
        city=city,
        zipcode=zipcode,
        mobile_number=mobile_number
    )

    # --------------------------------------------------
    # Create Account
    # --------------------------------------------------

    signup.create_account()

    # --------------------------------------------------
    # 10. Verify ACCOUNT CREATED
    # --------------------------------------------------

    signup.verify_account_created()

    signup.click_continue()

    # --------------------------------------------------
    # 11. Verify Logged in as username
    # --------------------------------------------------

    assert page.get_by_text(
        "Logged in as Iffat Jahan",
        exact=True
    ).is_visible()

    # --------------------------------------------------
    # 12. Click Cart
    # --------------------------------------------------
    # IMPORTANT:
    # Do NOT use:
    # page.locator('a[href="/view_cart"]').click()
    #
    # It matches both Cart and View Cart.
    # Use Page Object instead.

    home.click_cart()

    # --------------------------------------------------
    # 13. Click Proceed To Checkout
    # --------------------------------------------------

    cart.proceed_to_checkout()

    # --------------------------------------------------
    # 14. Verify Address Details
    #     and Review Your Order
    # --------------------------------------------------

    checkout.verify_checkout_page()

    # --------------------------------------------------
    # 15. Enter description/comment
    #     and click Place Order
    # --------------------------------------------------

    checkout.enter_comment(comment)

    checkout.place_order()

    # --------------------------------------------------
    # 16. Enter Payment Details
    # --------------------------------------------------

    payment.enter_payment_details(
        name_on_card=card_name,
        card_number=card_number,
        cvc=cvc,
        expiry_month=expiry_month,
        expiry_year=expiry_year
    )

    # --------------------------------------------------
    # 17. Click Pay and Confirm Order
    # --------------------------------------------------

    payment.pay_and_confirm_order()

    # --------------------------------------------------
    # 18. Verify Order Success
    # --------------------------------------------------

    payment.verify_order_success()

    # --------------------------------------------------
    # 19. Click Delete Account
    # --------------------------------------------------

    payment.delete_account()

    # --------------------------------------------------
    # 20. Verify ACCOUNT DELETED
    # --------------------------------------------------

    payment.verify_account_deleted()

    payment.click_continue()

