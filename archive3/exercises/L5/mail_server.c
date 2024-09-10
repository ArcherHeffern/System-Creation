#include <unistd.h> 
#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <signal.h>
#include <stdlib.h>
#include <fcntl.h>

#define BUFSIZE 1024
int database_pid = -1;

/*
Notes: 
- While I am using pipes in this example, in this circumstance you would probably use sockets due to their bidirectional capibilities
- There is no error handling in this program
*/

struct Options {
    // Options
};

void mail_server(int read_fd, int write_fd, struct Options *options);
void database();
void restart_database(int signo);
int parse_args(struct Options *options, int argc, char** args);
int parse_envp(struct Options *options, char** envp);
int parse_config_file(struct Options *options, char *filename);

struct Options options;
int db_read;
int db_write;

int main(int argc, char** argv, char** envp) {
    struct Options options;
    parse_args(&options, argc, argv);
    parse_envp(&options, envp);
    parse_config_file(&options, "/etc/techeducation_mail_server");
    parse_config_file(&options, "~/.techeducation_mail_server");

    // Setup communication channels
    int pipes1[2];
    int pipes2[2];
    pipe(pipes1);
    pipe(pipes2);
    db_read = pipes2[0];
    db_write = pipes1[1];

    if (fork() == 0) {
        mail_server(pipes1[0], pipes2[1], &options);
        exit(1);
    }
    database_pid = fork();
    if (database_pid == 0) {
        database();
        exit(1);
    }
    
    // Signal handler to restart database
    struct sigaction act;
    act.__sigaction_u.__sa_handler = restart_database;
    sigemptyset(&act.sa_mask);
    act.sa_flags = 0;
    sigaction(SIGINT, &act, 0);
    int stat_loc;
    wait(&stat_loc);
}

void create_account(int write_fd);
void authenticate(int write_fd);
void get_mail(int write_fd);
void send_mail(int write_fd);
char** tokenize(char* buffer);

void mail_server(int read_fd, int write_fd, struct Options *options) {
char buffer[BUFSIZE];
int buf_len;
char response[BUFSIZE];
int res_len;

while (1) {
    buf_len = read(STDIN_FILENO, buffer, BUFSIZE - 1);
    buffer[buf_len] = 0;
    char** tokens = tokenize(buffer);
    char* command = tokens[0];
    if (strcmp(command, "CREATEACCOUNT") == 0) {
        create_account(write_fd);
        } else if (strcmp(command, "AUTHENTICATE") == 0) {
            authenticate(write_fd);
        } else if (strcmp(command, "GETMAIL") == 0) {
            get_mail(write_fd);
        } else if (strcmp(command, "SENDMAIL") == 0) {
            send_mail(write_fd);
        }
    }
}

//#############################//
//##########Database###########//
//#############################//

// Each return -1 on failure, or the new length response
int create(char** tokens, char *response);
int get(char** tokens, char *response);
int update(char** tokens, char *response);
int delete(char** tokens, char *response);

void database() {
    // Setup
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
    chdir("/");

    // Run
    char buffer[BUFSIZE];
    char response[BUFSIZE];
    int res_len;
    int buf_len;

    while (1) {
        buf_len = read(db_read, buffer, BUFSIZE - 1);
        buffer[buf_len] = 0;
        char** tokens = tokenize(buffer);
        char* command = tokens[0];

        // Process command
        if (strcmp(command, "CREATE") == 0) {
            res_len = create(tokens, response);
        } else if (strcmp(command, "GET") == 0) {
            res_len = get(tokens, response);
        } else if (strcmp(command, "UPDATE") == 0) {
            res_len = update(tokens, response);
        } else if (strcmp(command, "DELETE") == 0) {
            res_len = delete(tokens, response);
        } else {
            strcpy(response, "INVALID");
            res_len = 8;
        }
        write(db_write, response, res_len);
    }
}

void restart_database(int s) {
    kill(database_pid, SIGQUIT);
    database();
}