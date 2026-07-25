from Pages.TestCase.test_case_page import TestCasePage


def test_testPage(page):
    testcase=TestCasePage(page)
    testcase.testcase_page()
    assert page.url=="https://automationexercise.com/test_cases"