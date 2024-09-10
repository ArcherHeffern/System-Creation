#include <stdio.h>

int main(int argc, char** argv, char** envp) {

    printf("Argument variables: \n");
    for (int i = 0; i < argc; i++) {
        printf("%s\n", argv[i]);
    }

    printf("\n");
    printf("Environment variables\n");
    while (*envp != 0) {
        printf("%s\n", *(envp++));
    }
}