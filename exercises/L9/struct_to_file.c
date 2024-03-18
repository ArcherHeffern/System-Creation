#include <stdio.h>
#include <stdlib.h>

// Define a struct representing a person
struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // Create an instance of the struct
    struct Person person = {"John Doe", 30, 175.5};

    // Open a binary file in write mode
    FILE *file = fopen("person_data.bin", "wb");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    // Write the struct to the file
    size_t bytes_written = fwrite(&person, sizeof(struct Person), 1, file);
    if (bytes_written != 1) {
        perror("Error writing to file");
        fclose(file);
        return EXIT_FAILURE;
    }

    // Close the file
    fclose(file);

    printf("Struct written to file successfully.\n");

    return EXIT_SUCCESS;
}