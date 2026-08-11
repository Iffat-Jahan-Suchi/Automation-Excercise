from pathlib import Path

from Locators.contact_us_locator import ContactUs
class Contact:
    def __init__(self,page):
        self.page=page
        self.locator=ContactUs(page)

    def contact_page(self,name,email,subject,msg,file_name):
        self.locator.contact_button.click()
        self.locator.name.fill(name)
        self.locator.email.fill(email)
        self.locator.subject.fill(subject)
        self.locator.msg.fill(msg)
        file_path = Path(__file__).resolve().parents[2] / "TestData" / file_name
        self.locator.upload.set_input_files(str(file_path))
        self.page.wait_for_timeout(3000)
        def handle_dialog(dialog):
            dialog.accept()
        self.page.on("dialog", handle_dialog)
        self.locator.submit.click()
        self.locator.success_msg.wait_for()
        return self.locator.success_msg.text_content().strip()

    def home(self):
        self.locator.home.click()
