#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/wait.h>
#include <assert.h>

#define BUFSIZE 128
#define EXT_SUCCESS 0
#define EXT_ERR_READ_STDIN 1
#define EXT_ERR_INVALID_COMMAND 2

char** str_split(char* a_str);
char** parse_args(char* buffer);

int main() {
    char buffer[BUFSIZE];
    char** args = parse_args(buffer);
    char* command = args[0];

    while (strcmp(command, "exit") != 0 && strcmp(command, "quit") != 0) {
        if (fork() == 0) {
            execvp(command, args);
            fprintf(stderr, "%s: Command not found\n", command);
            exit(EXT_ERR_INVALID_COMMAND);
        }
        int stat_loc;
        wait(&stat_loc);
        args = parse_args(buffer);
        command = args[0];
    }
    printf("Exiting...\n");
    exit(EXT_SUCCESS);
}

char** parse_args(char* buffer) {
    buffer[0] = 0;
    while (strlen(buffer) == 0) {
        printf("> ");
        if (fgets(buffer, BUFSIZE, stdin) == NULL) {
            fprintf(stderr, "Error reading stdin");
            exit(EXT_ERR_READ_STDIN);
        }
        buffer[strcspn(buffer, "\n")] = 0;
    }
    char** args = str_split(buffer);
    return args;
}

char** str_split(char* a_str) {
    char** result    = 0;
    size_t count     = 0;
    char* tmp        = a_str;
    char* last_comma = 0;
    char delim[2];
    const char a_delim = ' ';
    delim[0] = a_delim;
    delim[1] = 0;

    /* Count how many elements will be extracted. */
    while (*tmp)
    {
        if (a_delim == *tmp)
        {
            count++;
            last_comma = tmp;
        }
        tmp++;
    }

    /* Add space for trailing token. */
    count += last_comma < (a_str + strlen(a_str) - 1);

    /* Add space for terminating null string so caller
       knows where the list of returned strings ends. */
    count++;

    result = malloc(sizeof(char*) * count);

    if (result)
    {
        size_t idx  = 0;
        char* token = strtok(a_str, delim);

        while (token)
        {
            assert(idx < count);
            *(result + idx++) = strdup(token);
            token = strtok(0, delim);
        }
        assert(idx == count - 1);
        *(result + idx) = 0;
    }

    return result;
}
