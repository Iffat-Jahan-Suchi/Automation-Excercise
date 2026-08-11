from Locators.testCase_locator import TestcaseLoc
class CasesPage:
    def __init__(self,page):
        self.page=page
        self.locator=TestcaseLoc(page)
    def case_page(self):
        self.locator.test_case.click()
