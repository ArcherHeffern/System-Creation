#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "sqlite-amalgamation-3450200/sqlite3.h"
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <unistd.h>

#define EXT_SUCCESS 0
#define EXT_ERR_SOCKET 1
#define EXT_ERR_BIND 2
#define EXT_ERR_LISTEN 3
#define EXT_ERR_ACCEPT 4
#define EXT_ERR_SETSOCKOPT 5

#define RET_SUCCESS 0
#define RET_ERR_PREPARE 1

#define BUFSIZE 1024
#define PORT 5433

void handle_connection(int socket);
int execute(int socket, sqlite3** db, char* statement);
void print_result(int socket, int ret_status, char* statement);
void clean_database(int socket, sqlite3** db);

int main() {
    int s;
    int remote;
    struct sockaddr_in local_addr;

    if ((s = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Socket");
        exit(EXT_ERR_SOCKET);
    }

    const int enable = 1;
    if (setsockopt(s, SOL_SOCKET, SO_REUSEADDR, &enable, sizeof(int)) < 0) {
        perror("SetSockOpt");
        exit(EXT_ERR_SETSOCKOPT);
    }

    memset(&local_addr, 0, sizeof(local_addr));
    local_addr.sin_family = AF_INET;
    local_addr.sin_port = htons(PORT);
    local_addr.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    if (bind(s, &local_addr, sizeof(local_addr)) == -1) {
        perror("Bind");
        exit(EXT_ERR_BIND);
    }

    if (listen(s, 1) == -1) {
        perror("Listen");
        exit(EXT_ERR_LISTEN);
    }
    printf("Listening at loopback:%d\n", PORT);

    while (1) {
        if ((remote = accept(s, NULL, NULL)) == -1) {
            perror("Accept");
            exit(EXT_ERR_ACCEPT);
        }
        printf("Accepted Connection...\n");
        handle_connection(remote);
        printf("Remote Connection Ended\n");
    }
}

void handle_connection(int socket) {
    sqlite3 *db;
    char* statement;
    char buffer[BUFSIZE];
    int nread;

    sqlite3_open("Account", &db);
    clean_database(socket, &db);

    while (1) {
        write(socket, "> ", 3);
        nread = read(socket, buffer, BUFSIZE - 1);
        if (nread == 0) {
            break;
        }
        buffer[nread] = 0;
        if (strncmp("exit", buffer, 4) == 0) {
            close(socket);
            return;
        }
        execute(socket, &db, buffer);
    }
}

void clean_database(int socket, sqlite3** db) {
    char* statement; 
    statement = "DROP TABLE IF EXISTS Users;";
    execute(socket, db, statement);
    statement = "CREATE TABLE IF NOT EXISTS Users (userid int NOT NULL PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), password VARCHAR(255));";
    execute(socket, db, statement);
    statement = "INSERT INTO Users VALUES (0, 'Timmy', 'Turner', 'timmyturner@gmail.com', 'i_like_frogs');";
    execute(socket, db, statement);
    statement = "INSERT INTO Users VALUES (1, 'Jon', 'Sitlee', 'jonsits@gmail.com', 'i_like_otters');";
    execute(socket, db, statement);
    statement = "SELECT * FROM Users;";
    execute(socket, db, statement);
}

int execute(int socket, sqlite3** db, char* statement) {
    sqlite3_stmt *ppStmt;
    int ret_status;
    int user_id;
    char* first_name;
    char* last_name;
    char* email;
    char* password; 
    char* strp;
    int len;

    if ((ret_status = sqlite3_prepare_v2(*db, statement, -1, &ppStmt, NULL)) != SQLITE_OK) {
        len = asprintf(&strp, "Prepare (%d): %s\n", ret_status, statement);
        write(socket, strp, len);
        return RET_ERR_PREPARE;
    }
    while ((ret_status = sqlite3_step(ppStmt)) != SQLITE_DONE) {
        user_id = sqlite3_column_int(ppStmt, 0);
        len = asprintf(&strp, "User id: %d\n", user_id);
        write(socket, strp, len);
        first_name = sqlite3_column_text(ppStmt, 1);
        len = asprintf(&strp, "First name: %s\n", first_name);
        write(socket, strp, len);
        last_name = sqlite3_column_text(ppStmt, 2);
        len = asprintf(&strp, "Last name: %s\n", last_name);
        write(socket, strp, len);
        email = sqlite3_column_text(ppStmt, 3);
        len = asprintf(&strp, "Email: %s\n", email);
        write(socket, strp, len);
        password = sqlite3_column_text(ppStmt, 4);
        len = asprintf(&strp, "Password: %s\n", password);
        write(socket, strp, len);
        write(socket, "\n", 2);
    }
    print_result(socket, ret_status, statement);
    sqlite3_finalize(ppStmt);
    return RET_SUCCESS;
}

void print_result(int socket, int ret_status, char* statement) {
    if (ret_status == SQLITE_BUSY) {
        fprintf(stderr, "Busy: %s\n", statement);
    } else if (ret_status == SQLITE_ERROR) {
        fprintf(stderr, "Error: %s\n", statement);
    } else if (ret_status == SQLITE_MISUSE) {
        fprintf(stderr, "Misuse: %s\n", statement);
    } else if (ret_status == SQLITE_ROW) {
        printf("Row avaliable\n");
        return;
    }
    if (ret_status != SQLITE_DONE) {
        fprintf(stderr, "Something is wrong (%d): %s\n", ret_status, statement);
    }
}