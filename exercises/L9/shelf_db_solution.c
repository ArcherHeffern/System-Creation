#include <stdio.h>
#include <string.h>

/*
This is a very basic example and lacks many features of a real database, such as persistent storage, error handling, and efficient searching mechanisms. However, it demonstrates the core idea of CRUD operations on a simple data structure in C.
*/

#define MAX_BOOKS 10

typedef struct {
    int id;
    char name[50];
    int age;
} Book;

Book database[MAX_BOOKS];
int current_id = 0;

// Create a new person
int create_person(char* name, int age) {
    if (current_id == MAX_BOOKS) {
        printf("Database is full.\n");
        return -1;
    }

    Book new_person;
    new_person.id = current_id;
    strcpy(new_person.name, name);
    new_person.age = age;

    database[current_id++] = new_person;
    return new_person.id;
}

// Read (get) a person by ID
Book* get_person(int id) {
    for (int i = 0; i < current_id; i++) {
        if (database[i].id == id) {
            return &database[i];
        }
    }
    return NULL;
}

// Update a person
void update_person(int id, char* name, int age) {
    Book* person = get_person(id);
    if (person != NULL) {
        strcpy(person->name, name);
        person->age = age;
        printf("Book with ID %d updated.\n", id);
    } else {
        printf("Book with ID %d not found.\n", id);
    }
}

// Delete a person
void delete_person(int id) {
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
void list_people() {
    printf("List of people:\n");
    for (int i = 0; i < current_id; i++) {
        printf("ID: %d, Name: %s, Age: %d\n", database[i].id, database[i].name, database[i].age);
    }
}

int main() {
    create_person("Alice", 30);
    create_person("Bob", 25);
    list_people();

    update_person(0, "Alice Smith", 31);
    list_people();

    delete_person(1);
    list_people();

    return 0;
}