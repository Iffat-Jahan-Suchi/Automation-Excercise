class ConfirmPopUpLoc:
    def __init__(self, page):
        self.page = page
        self.confirm_alertBtn = page.locator("//button[@id='confirm']")
        self.accept_text=page.get_by_text("OK it is!",exact=True)
        self.cancel_text=page.get_by_text("Cancel it is!",exact=True)
