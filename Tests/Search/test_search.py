from Pages.Search.Search import Search


def test_search(page):
    search=Search(page)
    search.search_item("polo")