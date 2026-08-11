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


        #first product
        self.first_product = page.locator(".product-image-wrapper").nth(0)
        self.first_name = page.locator(".productinfo p").nth(0)
        self.first_price = page.locator(".productinfo h2").nth(0)
        self.add_cart=self.page.locator("//div[@class='col-sm-9 padding-right']//div[2]//div[1]//div[1]//div[2]//div[1]//a[1]")

        #2nd product
        self.second_product = page.locator(".product-image-wrapper").nth(1)
        self.second_name = page.locator(".productinfo p").nth(1)
        self.second_price = page.locator(".productinfo h2").nth(1)
        self.add_sec_cart=self.page.locator("//div[3]//div[1]//div[1]//div[2]//div[1]//a[1]")

        #add to cart and continue shop
        self.modal =self.page.locator("#cartModal")
        self.continue_btn=self.modal.get_by_role("button", name="Continue Shopping")
        self.view_cart_btn=self.modal.locator("//u[normalize-space()='View Cart']")

        #home page view product loc
        self.view_product=page.locator("a[href='/product_details/1']")
        self.product_information = page.locator(".product-information")
        self.increment_qty_btn=page.locator("#quantity")
        self.add_to_cart = page.locator("button.cart")
        self.view_cart = page.locator("u")
