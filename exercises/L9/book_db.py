
#TODO: Implement lookup feature for chapters
#TODO: Create user interface
#TODO: Create a protocol to write to plain text file
#TODO: Create Advanced protocol to write to binary file
# Protocol: 2 bytes: Size, 2 bytes class, unknown bytes-Content

DB_PATH = "bookdb.db"
class Page:
    def __init__(self, page_number, content):
        self.page_number: int = page_number
        self.content: str = content

    def serialize(self):
        serialized_str = bytes([self.page_number]) + self.content.encode()
        len_str = len(serialized_str)
        return bytes([len_str]) + serialized_str

    def deserialize(self):
        pass


def create_page(page: Page):
    with open(DB_PATH, "wba+") as f:
        f.write(page.serialize())

def read_pages():
    with open(DB_PATH, 'rb+') as f:
        f.read()

def get_page_by_number(page_number: int):
    with open(DB_PATH, "r") as f:
        f.read()
    for page in page_database:
        if page.page_number == page_number:
            return page

