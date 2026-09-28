from Pages.FileUploadPage.FileUploadPage import FileUploadPage


def test_upload_file(page):
    page.goto("https://www.playwrightautomation.com/practice.html?utm_source=chatgpt.com#section-upload-standard")
    file_upload=FileUploadPage(page)
    file_upload.upload_file("TestData/sample.pdf")