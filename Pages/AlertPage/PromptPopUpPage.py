from Locators.AlertLoc.PromptAlertLoc import PromptAlertLoc


class PromptAlertPage:
    def __init__(self, page):
        self.page = page
        self.promptLoc=PromptAlertLoc(page)

    def prompt_popup(self,val):
        self.page.once("dialog", lambda dialog: dialog.accept(val))
        self.promptLoc.prompt_alert.click()
        assert self.promptLoc.input_text.is_visible()

    def prompt_cancel(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.promptLoc.prompt_alert.click()
        assert self.promptLoc.input_text.is_visible()
