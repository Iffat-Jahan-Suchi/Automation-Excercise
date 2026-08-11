
from Locators.search_locator import SearchLoc


class Search:
    def __init__(self,page):
        self.page=page
        self.locator=SearchLoc(page)

    def search_item(self,name):
            self.locator.product.click()
            assert self.page.url == "https://automationexercise.com/products"
            self.page.wait_for_timeout(2000)
            self.locator.search_field.fill(name)
            self.page.wait_for_timeout(2000)
            self.locator.search_btn.click()
            assert self.locator.search_title.is_visible()
            assert self.locator.search_items.is_visible()

