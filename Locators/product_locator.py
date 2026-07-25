class ProductLoc:
    def __init__(self,page):
        self.page=page

        self.product=self.page.locator("a[href='/products']")
        self.product_title=self.page.locator("h2.title")
        self.product_list=self.page.locator(".features_items")
        self.first_item = page.locator(".product-information p").first
        self.first_view_product = page.locator("a[href='/product_details/1']")
        self.name = page.locator(".product-information h2")
        self.category = page.locator(".product-information p").first
        self.price = page.locator(".product-information span span")
        self.availability = page.locator("//b[normalize-space()='Availability:']")
        self.condition = page.locator("//b[normalize-space()='Condition:']")
        self.brand = page.locator("//b[normalize-space()='Brand:']")