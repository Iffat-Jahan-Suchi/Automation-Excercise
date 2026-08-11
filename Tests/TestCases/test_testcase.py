from Pages.TestCase.testCase_page import CasesPage


def test_testPage(page):
    testcase=CasesPage(page)
    testcase.case_page()
    assert page.url=="https://automationexercise.com/test_cases"