class IframeLoc:

    def __init__(self, page):
        self.page = page

        self.iframe = "//iframe[@data-testid='iframe']"
        self.search = "//input[@placeholder='Filter by product name']"
        self.filter_btn = "//button[@data-testid='filter-button']"