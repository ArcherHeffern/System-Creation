#include "sqlite-amalgamation-3450200/sqlite3.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define EXT_ERR_PREPARE 1
#define EXT_ERR_BUSY 2
#define EXT_ERR_ERROR 3
#define EXT_ERR_MISUSE 4

void execute(sqlite3** db, char* statement);
void print_result(int ret_status, char* statement);

int main() {
    sqlite3 *db;
    char* statement;

    sqlite3_open("Account", &db);
    statement = "DROP TABLE IF EXISTS Users;";
    execute(&db, statement);
    statement = "CREATE TABLE IF NOT EXISTS Users (userid int NOT NULL PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), email VARCHAR(255), password VARCHAR(255));";
    execute(&db, statement);
    statement = "INSERT INTO Users VALUES (0, 'Timmy', 'Turner', 'timmyturner@gmail.com', 'i_like_frogs');";
    execute(&db, statement);
    statement = "INSERT INTO Users VALUES (1, 'Jon', 'Sitlee', 'jonsits@gmail.com', 'i_like_otters');";
    execute(&db, statement);
    statement = "SELECT * FROM Users;";
    execute(&db, statement);
    sqlite3_close(db);
}

void execute(sqlite3** db, char* statement) {
    sqlite3_stmt *ppStmt;
    int ret_status;
    int user_id;
    char* first_name;
    char* last_name;
    char* email;
    char* password; 

    if ((ret_status = sqlite3_prepare_v2(*db, statement, -1, &ppStmt, NULL)) != SQLITE_OK) {
        printf("Prepare (%d): %s\n", ret_status, statement);
        exit(EXT_ERR_PREPARE);
    }
    while ((ret_status = sqlite3_step(ppStmt)) != SQLITE_DONE) {
        user_id = sqlite3_column_int(ppStmt, 0);
        first_name = sqlite3_column_text(ppStmt, 1);
        last_name = sqlite3_column_text(ppStmt, 2);
        email = sqlite3_column_text(ppStmt, 3);
        password = sqlite3_column_text(ppStmt, 4);
        printf("User id: %d\n", user_id);
        printf("First name: %s\n", first_name);
        printf("Last name: %s\n", last_name);
        printf("Email: %s\n", email);
        printf("Password: %s\n", password);
        printf("\n");
    }
    print_result(ret_status, statement);
    sqlite3_finalize(ppStmt);

}

void print_result(int ret_status, char* statement) {
    if (ret_status == SQLITE_BUSY) {
        fprintf(stderr, "Busy: %s\n", statement);
        exit(EXT_ERR_BUSY);
    } else if (ret_status == SQLITE_ERROR) {
        fprintf(stderr, "Error: %s\n", statement);
        exit(EXT_ERR_ERROR);
    } else if (ret_status == SQLITE_MISUSE) {
        fprintf(stderr, "Misuse: %s\n", statement);
        exit(EXT_ERR_MISUSE);
    } else if (ret_status == SQLITE_ROW) {
        printf("Row avaliable\n");
        return;
    }
    if (ret_status != SQLITE_DONE) {
        fprintf(stderr, "Something is wrong (%d): %s\n", ret_status, statement);
    }
}