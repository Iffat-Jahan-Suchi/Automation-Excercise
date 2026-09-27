class AlertPopUpLoc:
    def __init__(self,page):
        self.page=page
        self.alertBtn=page.locator("//button[@id='alert']")
        