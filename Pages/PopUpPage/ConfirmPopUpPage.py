from playwright.sync_api import expect

from Locators.PopUpLoc.ConfirmPopUpLoc import ConfirmPopUpLoc


class ConfirmPopUpPage:
    def __init__(self,page):
        self.page=page
        self.confirmLoc=ConfirmPopUpLoc(page)

    def confirm_popup(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.confirmLoc.confirm_alertBtn.click()
        expect(self.confirmLoc.accept_text).to_be_visible()


    def cancel_popup(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.confirmLoc.confirm_alertBtn.click()
        print(self.page.locator("#confirmResult").inner_text())
        expect(self.confirmLoc.cancel_text).to_be_visible()