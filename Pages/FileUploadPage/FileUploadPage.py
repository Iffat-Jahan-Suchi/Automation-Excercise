from Locators.FileUploadLoc.FileUoloadLoc import FileUpLoadLoc


class FileUploadPage:
    def __init__(self,page):
        self.page=page
        self.fileUploadLoc=FileUpLoadLoc(page)

    def upload_file(self,path):
        self.fileUploadLoc.choose_file_path.set_input_files(path)

