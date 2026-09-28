class FileUpLoadLoc:
    def __init__(self,page):
        self.page=page
        self.choose_file_path = page.locator("//input[@id='upload-single']")