class SearchLoc:
    def __init__(self,page):
        self.page=page


        self.product=self.page.locator("//a[@href='/products']")
        self.search_field=self.page.locator("//input[@id='search_product']")
        self.search_btn=self.page.locator("#submit_search")
        self.search_title=self.page.locator("//h2[@class='title text-center']")
        self.search_items=self.page.locator(".features_items")
