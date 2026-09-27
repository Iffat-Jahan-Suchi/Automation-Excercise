from Locators.PopUpLoc.AlertPopUpLoc import AlertPopUpLoc


class AlertPopUpPage:
    def __init__(self,page):
        self.page=page
        self.alertLoc=AlertPopUpLoc(page)

    def click_alert_popup(self):
        self.page.on("dialog",lambda dialog:dialog.accept())
        self.alertLoc.alertBtn.click()