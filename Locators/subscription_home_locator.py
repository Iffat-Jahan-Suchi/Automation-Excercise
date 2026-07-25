class SubscriptionHomeLoc:
    def __init__(self,page):
        self.page=page

        self.footer=self.page.locator("#footer")
        self.subscription=self.page.locator("//h2[normalize-space()='Subscription']")
        self.email=self.page.locator("#susbscribe_email")
        self.arrow=self.page.locator("#subscribe")
