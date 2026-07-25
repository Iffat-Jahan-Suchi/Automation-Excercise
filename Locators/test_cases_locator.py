class TestCaseLoc:
    def __init__(self,page):
        self.page=page

        self.test_case=self.page.locator("a[href='/test_cases']").first