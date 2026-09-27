from Pages.PopUpPage.AlertPopUpPage import AlertPopUpPage
from Pages.PopUpPage.ConfirmPopUpPage import ConfirmPopUpPage
from Pages.PopUpPage.PromptPopUpPage import PromptPopUpPage


def test_alertpopup(page):
    page.goto("https://practice-automation.com/popups/")
    alertPopUp=AlertPopUpPage(page)
    alertPopUp.click_alert_popup()


def test_confirm_cancel_popup(page):
    page.goto("https://practice-automation.com/popups/")
    confirmCancel=ConfirmPopUpPage(page)
    confirmCancel.confirm_popup()
    confirmCancel.cancel_popup()

def test_prompt_alert(page):
    page.goto("https://practice-automation.com/popups/")
    prompt_alert=PromptPopUpPage(page)
    prompt_alert.prompt_popup("jahan")
    prompt_alert.prompt_cancel()