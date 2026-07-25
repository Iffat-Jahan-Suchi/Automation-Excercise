from Locators.subscription_home_locator import SubscriptionHomeLoc


class SubscriptionHome:
    def __init__(self,page):
        self.page=page
        self.locator=SubscriptionHomeLoc(page)

    def subsciption_home(self,email):
        self.locator.footer.scroll_into_view_if_needed()
        assert self.locator.subscription.is_visible()
        self.page.wait_for_timeout(3000)
        self.locator.email.fill(email)
        self.locator.arrow.click()