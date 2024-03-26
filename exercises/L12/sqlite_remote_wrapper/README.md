# Dependencies
Install [SQLite amalgamation-3450200.zip source code](https://www.sqlite.org/download.html) and unzip into this directory

# Compile
`gcc -o sqlite_wrapper sqlite_wrapper.c sqlite-amalgamation-3450200/sqlite3.c`

# Run
`./sqlite_wrapper`

# Usage
Connect to the sqlite server using netcat...
```bash
nc 127.0.0.1 5433
```
You can now make SQL queries remotely. The server has a default table called Users with some data filled in. 

# Sources
- https://www.sqlite.org/cintro.html

# Notes
Doing this may be considered a sin, because by design, SQLite is not designed to be put on a server. As a result, our server will only handle 1 user at a time. 