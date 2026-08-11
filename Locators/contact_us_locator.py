class ContactUs:
    def __init__(self,page):
        self.page=page

        self.contact_button=self.page.locator("//a[normalize-space()='Contact us']")
        self.name=self.page.locator("//input[@placeholder='Name']")
        self.email=self.page.locator("//input[@placeholder='Email']")
        self.subject=self.page.locator("//input[@placeholder='Subject']")
        self.msg=self.page.locator("//textarea[@id='message']")
        self.upload = page.locator("input[type='file']")
        self.submit=self.page.locator("//input[@name='submit']")
        self.success_msg=self.page.locator("//div[@class='status alert alert-success']")
        self.home=self.page.locator("//a[@class='btn btn-success']")



