from Locators.test_cases_locator import TestCaseLoc
class TestCasePage:
    def __init__(self,page):
        self.page=page
        self.locator=TestCaseLoc(page)

    def testcase_page(self):
        self.locator.test_case.click()
