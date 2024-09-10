#include "libpq-fe.h"
#include <stdio.h>
#include <stdlib.h>

#define EXT_ERR_BAD_CONNECTION 1
#define EXT_ERR_BAD_COMMAND 2
#define EXT_SUCCESS 0

static void exit_nicely(PGconn *conn);
PGresult* execute_nicely(PGconn *conn, const char *query, const char* errorMsg);

int main() {
    PGconn *conn;
    PGresult *res;
    int nFields;
    int i;
    int j;

    conn = PQconnectdb("postgresql://postgres:password@");
    if (PQstatus(conn) != CONNECTION_OK) {
        fprintf(stderr, "%s", PQerrorMessage(conn));
        exit(EXT_ERR_BAD_CONNECTION);
    }

    res = execute_nicely(conn, "BEGIN", "BEGIN command failed");
    PQclear(res);

    res = execute_nicely(conn, "DROP TABLE IF EXISTS Users;", "Drop Users Table Failed");
    PQclear(res);

    res = execute_nicely(conn, "CREATE TABLE Users (userid VARCHAR(64) PRIMARY KEY, first_name VARCHAR(64), last_name VARCHAR(64), email VARCHAR(64), password VARCHAR(64));", "Create Users Table Failed");
    PQclear(res);

    res = execute_nicely(conn, "INSERT INTO Users VALUES (1, 'Timmy', 'Turner', 'timmyturner@gmail.com', 'i_like_frogs');", "Create Timmy Record Failed");
    PQclear(res);

    res = execute_nicely(conn, "INSERT INTO Users VALUES (2, 'Jon', 'Sitdlee', 'jonsits@ihop.com', 'i_like_otters');", "Create Jon Record Failed");
    PQclear(res);

    res = execute_nicely(conn, "INSERT INTO Users VALUES (3, 'Fred', 'Krueger', 'wesCraven@aol.com', 'elm_street_frights');", "Create Freddy Record Failed");
    PQclear(res);

    /*
     * Fetch rows from pg_database, the system catalog of databases
     */
    res = execute_nicely(conn, "DECLARE myportal CURSOR FOR SELECT * from Users;", "DECLARE CURSOR Failed");
    PQclear(res);

    res = execute_nicely(conn, "FETCH ALL IN myportal;", "FETCH ALL Failed");

    /* first, print out the attribute names */
    nFields = PQnfields(res);
    for (i = 0; i < nFields; i++)
        printf("%-15s", PQfname(res, i));
    printf("\n\n");

    /* next, print out the rows */
    for (i = 0; i < PQntuples(res); i++)
    {
        for (j = 0; j < nFields; j++)
            printf("%-15s", PQgetvalue(res, i, j));
        printf("\n");
    }

    PQclear(res);

    res = PQexec(conn, "CLOSE myportal");
    PQclear(res);

    res = PQexec(conn, "END");
    PQclear(res);

    PQfinish(conn);

    return EXT_SUCCESS;
}
PGresult* execute_nicely(PGconn *conn, const char *query, const char* errorMsg) {
    PGresult *res;

    res = PQexec(conn, query);
    ExecStatusType status = PQresultStatus(res);
    if (status != PGRES_TUPLES_OK && status != PGRES_COMMAND_OK) {
        fprintf(stderr, "%s: %s", errorMsg, PQerrorMessage(conn));
        PQclear(res);
        exit_nicely(conn);
    }
    return res;
}

static void exit_nicely(PGconn *conn) {
    PQfinish(conn);
    exit(EXT_ERR_BAD_COMMAND);
}