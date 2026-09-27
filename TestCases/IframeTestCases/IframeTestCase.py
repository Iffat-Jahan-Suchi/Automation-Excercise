from Pages.IFramePage.iFramePage import IframePage


def test_iframe(page):
    page.goto("https://commitquality.com/practice-iframe")
    iframe = IframePage(page)
    iframe.search("Product 1")
    iframe.click_filter()