from Pages.FileDownLoadPage.FileDownLoadPage import FileDownLoadPage


def test_download(page):
    page.goto("https://www.playwrightautomation.com/practice.html?utm_source=chatgpt.com#section-upload-downloads")
    download_my_file=FileDownLoadPage(page)
    file_path=download_my_file.download_file()
    assert file_path.exists()

