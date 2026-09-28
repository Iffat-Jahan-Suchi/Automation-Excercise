from Pages.AlertPage.AlertPage import AlertPage
from Pages.AlertPage.ConfirmPopUpPage import ConfirmAlertPage
from Pages.AlertPage.PromptPopUpPage import PromptAlertPage


def test_alert(page):
    page.goto("https://practice-automation.com/popups/")
    alertPopUp=AlertPage(page)
    alertPopUp.click_alert_popup()


def test_confirm_cancel_alert(page):
    page.goto("https://practice-automation.com/popups/")
    confirmCancel=ConfirmAlertPage(page)
    confirmCancel.confirm_popup()
    confirmCancel.cancel_popup()

def test_input_alert(page):
    page.goto("https://practice-automation.com/popups/")
    prompt_alert=PromptAlertPage(page)
    prompt_alert.prompt_popup("jahan")
    prompt_alert.prompt_cancel()