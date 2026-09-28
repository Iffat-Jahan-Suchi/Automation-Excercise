from pathlib import Path

from pip._internal.commands import download

from Locators.FileDownLoadLoc.FileDownLoadLoc import FileDownLoadLoc


class FileDownLoadPage:
    def __init__(self,page):
        self.page=page
        self.downLoadLoc=FileDownLoadLoc(page)

    def download_file(self):
        with self.page.expect_download() as download_info:
            self.downLoadLoc.download.click()
        download = download_info.value
        download_folder = Path("Download")
        download_folder.mkdir(exist_ok=True)
        file_path = download_folder / download.suggested_filename
        download.save_as(file_path)
        return file_path