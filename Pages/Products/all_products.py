from Locators.product_locator import ProductLoc


class Products:
    def __init__(self,page):
        self.page=page
        self.locator=ProductLoc(page)

    def all_product(self):
        self.locator.product.click()
        assert self.page.url == "https://automationexercise.com/products"
        assert self.locator.product_title.is_visible()
        assert self.locator.product_list.is_visible()
        self.locator.first_view_product.click()
        assert self.page.url=="https://automationexercise.com/product_details/1"
        assert self.locator.name.is_visible()
        assert self.locator.category.is_visible()
        assert self.locator.price.is_visible()
        assert self.locator.availability.is_visible()
        assert self.locator.condition.is_visible()
        assert self.locator.brand.is_visible()


