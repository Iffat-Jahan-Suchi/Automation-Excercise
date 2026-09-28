class FileDownLoadLoc:
    def __init__(self,page):
        self.page=page
        self.download=page.locator("//a[@id='btn-download-csv']")