#include <stdio.h>
#include <stdlib.h>

int main() {
    // Define and initialize the array
    int numbers[] = {1, 2, 3, 4, 5};
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);

    // Open a binary file for writing
    FILE *file = fopen("output.bin", "wb");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return EXIT_FAILURE;
    }

    // Write the array to the file
    size_t elementsWritten = fwrite(numbers, sizeof(int), arraySize, file);
    if (elementsWritten != arraySize) {
        fprintf(stderr, "Error writing to file.\n");
        fclose(file);
        return EXIT_FAILURE;
    }

    // Close the file
    fclose(file);

    printf("Array written to disk successfully.\n");
    return EXIT_SUCCESS;
}