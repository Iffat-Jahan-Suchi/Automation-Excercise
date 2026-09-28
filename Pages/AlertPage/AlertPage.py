from Locators.AlertLoc.AlertLoc import AlertLoc


class AlertPage:
    def __init__(self,page):
        self.page=page
        self.alertLoc=AlertLoc(page)

    def click_alert_popup(self):
        self.page.on("dialog",lambda dialog:dialog.accept())
        self.alertLoc.alertBtn.click()