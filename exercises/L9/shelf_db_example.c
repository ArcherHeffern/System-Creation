#include <stdio.h>
#include <string.h>

/*
This is a very basic example and lacks many features of a real database, such as persistent storage, error handling, and efficient searching mechanisms. However, it demonstrates the core idea of CRUD operations on a simple data structure in C.

Improvements: 
1. Implement missing methods
2. Implement multiple data types
2. Implement creation of any data types
2. Relationship between multiple data types
2. Implement persistance - single data type
    * Store to file between operations
    * Load from file
3. Implement multiple data types
4. Implement user Interface

5. More advanced querying
6. Faster querying

Advanced Features: 
- Error recovery
- Btrees
- Daemonize
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

// Read (get) a book by ID
Book* read_person(int id) {
    return NULL;
}

void update_book(int id, char* name, char* contents) {
    return NULL;
} 

int delete_book(int id) {
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
    // TODO: Create User Interface
    create_person("Alice", 30);
    create_person("Bob", 25);
    list_people();

    update_person(0, "Alice Smith", 31);
    list_people();

    delete_person(1);
    list_people();

    return 0;
}