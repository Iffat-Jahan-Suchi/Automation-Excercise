class SubscriptionHomeLoc:
    def __init__(self,page):
        self.page=page

        #home locator
        self.footer=self.page.locator("#footer")
        self.subscription=self.page.locator("//h2[normalize-space()='Subscription']")
        self.email=self.page.locator("#susbscribe_email")
        self.arrow=self.page.locator("#subscribe")

        #cart locator
        self.cart_button=page.locator("//a[normalize-space()='Cart']")
        self.success_msg=page.locator("#success-subscribe")

