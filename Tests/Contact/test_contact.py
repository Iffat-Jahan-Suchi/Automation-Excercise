from Pages.Contact.contact_info import Contact

def test_contact(page):
    contact=Contact(page)
    message =contact.contact_page("jahan","ij@gmail.com","automation testing","Good luck","sample.pdf")
    assert message == "Success! Your details have been submitted successfully."
    page.wait_for_timeout(2000)
    contact.home()