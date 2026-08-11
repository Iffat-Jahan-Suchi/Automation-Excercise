from Locators.subscription_home_locator import SubscriptionHomeLoc


class SubscriptionHome:
    def __init__(self,page):
        self.page=page
        self.locator=SubscriptionHomeLoc(page)

    def subscription_home(self,email):
        self.locator.footer.scroll_into_view_if_needed()
        assert self.locator.subscription.is_visible()
        self.page.wait_for_timeout(3000)
        self.locator.email.fill(email)
        self.locator.arrow.click()

    def subscription_cart(self,email):
        self.locator.cart_button.click()
        assert self.locator.subscription.is_visible()
        self.page.wait_for_timeout(3000)
        self.locator.email.fill(email)
        self.locator.arrow.click()
        assert self.locator.success_msg.is_visible()