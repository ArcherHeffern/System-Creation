#include <stdio.h>
#include <string.h>

/*
This is a very basic example and lacks many features of a real database, such as persistent storage, error handling, and efficient searching mechanisms. However, it demonstrates the core idea of CRUD operations on a simple data structure in C.
*/

#define MAX_BOOKS 10

typedef struct {
    int id;
    char name[50];
    char contents[1024];
} Book;

Book database[MAX_BOOKS];
int current_id = 0;

// Create a new person
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

// Read (get) a person by ID
Book* get_book(int id) {
    for (int i = 0; i < current_id; i++) {
        if (database[i].id == id) {
            return &database[i];
        }
    }
    return NULL;
}

// Update a person
void update_book(int id, char* name, char* contents) {
    Book* person = get_book(id);
    if (person != NULL) {
        strcpy(person->name, name);
        strcpy(person->contents, contents);
        printf("Book with ID %d updated.\n", id);
    } else {
        printf("Book with ID %d not found.\n", id);
    }
}

void delete_book(int id) {
    int found = 0;
    for (int i = 0; i < current_id; i++) {
        if (database[i].id == id) {
            found = 1;
        }
        if (found && i + 1 < current_id) {
            database[i] = database[i + 1];
        }
    }

    if (found) {
        current_id--;
        printf("Book with ID %d deleted.\n", id);
    } else {
        printf("Book with ID %d not found.\n", id);
    }
}

// List all people
void list_books() {
    printf("List of people:\n");
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