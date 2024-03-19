
#TODO: Implement lookup feature for chapters
#TODO: Create user interface

class Page:
    page_number: int
    content: str

page_database: list[Page] = []

def create_page(page: Page):
    page_database.append(page)

def get_page_by_number(page_number: int):
    for page in page_database:
        if page.page_number == page_number:
            return page

