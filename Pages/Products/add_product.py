from Locators.product_locator import ProductLoc


class AddProducts:
    def __init__(self,page):
        self.page=page
        self.locator=ProductLoc(page)

    def add_first_product(self):
        self.locator.product.click()
        assert self.page.url == "https://automationexercise.com/products"
        name =" ".join(self.locator.first_name.inner_text().split())
        price = self.locator.first_price.inner_text()
        self.page.mouse.wheel(0, 500)
        self.locator.first_product.hover()
        self.locator.add_cart.click()
        self.locator.modal.wait_for(state="visible")
        self.locator.continue_btn.click()
        return name,price

    def add_second_product(self):
        name =" ".join(self.locator.second_name.inner_text().split())
        price = self.locator.second_price.inner_text()
        self.page.mouse.wheel(0, 500)
        self.locator.second_product.hover()
        self.locator.add_sec_cart.click()
        self.locator.view_cart_btn.click()
        self.page.wait_for_timeout(3000)
        return name,price

