#include <stdio.h>
#include <string.h>

#define MAX_BOOKS 10

typedef struct {
    int id;
    char name[50];
    char contents[1024];
} Book;

Book database[MAX_BOOKS];
int current_id = 0;

int create_book(char* name, char* contents) {
    if (current_id == MAX_BOOKS) {
        printf("Database is full.\n");
        return -1;
    }

    Book new_book;
    new_book.id = current_id;
    strcpy(new_book.name, name);
    strcpy(new_book.contents, contents);

    database[current_id++] = new_book;
    return new_book.id;
}

// Read (get) a book by ID
Book* read_book(int id) {
    return NULL;
}

void update_book(int id, char* name, char* contents) {
    printf("Update Book not Implemented\n");
    return NULL;
} 

int delete_book(int id) {
    printf("Delete Book not Implemented\n");
    return NULL;
}

// List all people
void list_books() {
    printf("List of books:\n");
    for (int i = 0; i < current_id; i++) {
        printf("ID: %d, Name: %s, Contents: %s\n", database[i].id, database[i].name, database[i].contents);
    }
}

int main() {
    create_book("Fish", "1 Fish 2 Fish Red Fish Blue Fish");
    create_book("Bob", "Hello my name is bob and this is my book");
    list_books();

    update_book(0, "Alice Smith", "This me book by Alice");
    list_books();

    delete_book(1);
    list_books();

    return 0;
}