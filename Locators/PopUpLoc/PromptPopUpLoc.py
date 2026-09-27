class PromptPopUpLoc:
    def __init__(self,page):
        self.page=page
        self.prompt_alert=page.locator("//b[normalize-space()='Prompt Popup']")
        self.input_text=page.locator("#promptResult")
        self.cancel_text=page.get_by_text("#Fine, be that way...",exact=True)

