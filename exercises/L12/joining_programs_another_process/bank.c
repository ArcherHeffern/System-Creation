#include "libpq-fe.h"
#include <stdio.h>
#include <stdlib.h>

#define EXT_ERR_BAD_CONNECTION 1

int main() {
    PGconn *db = PQconnectdb("postgresql://postgres:password@127.0.0.1:5432/bank");
    if (PQstatus(db) == CONNECTION_BAD) {
        fprintf(stderr, "Bad Connection\n");
        exit(EXT_ERR_BAD_CONNECTION);
    }
}