#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <sys/wait.h>
#include <assert.h>
#include "sockutils.h"

#define BUFSIZE 128
#define EXT_SUCCESS 0
#define EXT_ERR_READ_STDIN 1
#define EXT_ERR_INVALID_COMMAND 2

char** str_split(char* a_str);
char** parse_args(char* buffer);

int main() {
    char buffer[BUFSIZE];
    char** args;
    char* command;
	int server;
	int client;
	char* port;

	port = "80";
	server = make_server(port, 5);
	printf("Listening at 0.0.0.0:%s\n", port);
	
	while ((client = server_accept(server)) > 0) {
		if (fork() == 0) {
			dup2(client, 0);
			dup2(client, 1);
			dup2(client, 2);

			args = parse_args(buffer);
			command = args[0];

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
	}
}

char** parse_args(char* buffer) {
    buffer[0] = 0;
    while (strlen(buffer) == 0) {
        printf("> ");
		fflush(stdout);
        if (fgets(buffer, BUFSIZE, stdin) == NULL) {
            fprintf(stderr, "Error reading stdin");
            exit(EXT_ERR_READ_STDIN);
        }
        buffer[strcspn(buffer, "\n")] = 0;
    }
    char** args = str_split(buffer);
    return args;
}

char** str_split(char* cmd) {
	int size = 5; 
	char **tokens = malloc(size * sizeof(char *));
	char delimiter[] = " \n";

	tokens[0] = strtok(cmd, delimiter);
	for (int i = 1; tokens[i-1] != NULL; i++) {
		if (i >= size) {
			size *= 2;
			if ((tokens = realloc(tokens, size * sizeof(char *))) == NULL) {
				fprintf(stderr, "Out of memory\n");
				exit(1);
			}
		}
		tokens[i] = strtok(NULL, delimiter);
	}

	return tokens;
}
