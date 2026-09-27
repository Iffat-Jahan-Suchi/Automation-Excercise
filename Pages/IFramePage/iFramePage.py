from Locators.IframeLoc.iFrameLoc import IframeLoc


class IframePage:

    def __init__(self, page):
        self.page = page
        self.iframeLoc = IframeLoc(page)

    def switch_to_iframe(self):
        return self.page.frame_locator(self.iframeLoc.iframe)

    def search(self, name):
        frame = self.switch_to_iframe()

        frame.locator(self.iframeLoc.search).fill(name)

    def click_filter(self):
        frame = self.switch_to_iframe()

        frame.locator(self.iframeLoc.filter_btn).click()