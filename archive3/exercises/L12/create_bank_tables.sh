#!/usr/bin/env bash

commands=$(cat << EOF
CREATE TABLE User (userid INT PRIMARY KEY, name VARCHAR(64), password VARCHAR(64), status INT);
CREATE TABLE Account (accountid INT PRIMARY KEY, userid INT, balance INT, FOREIGN KEY(userid) REFERENCES User(userid));

INSERT INTO User VALUES (0, 'Tim', 'i_like_frogs', TRUE);
INSERT INTO User VALUES (1, 'Sarah', 'i_like_otters', FALSE);
INSERT INTO User VALUES (2, 'Taylor', 'i_like_cheese', FALSE);
INSERT INTO User VALUES (3, 'Tom', 'i_like_kermit', TRUE);

INSERT INTO Account VALUES (0, 0, 10);
INSERT INTO Account VALUES (1, 0, -100);
INSERT INTO Account VALUES (2, 2, 66);
INSERT INTO Account VALUES (3, 1, 2);
EOF
)

dbname=Bank

if ! command -v sqlite3 &> /dev/null; then
    echo "sqlite3 could not be found"
    exit 1
fi

if [ -e $dbname ]; then
    read -p "${dbname} exists in this directory, are you sure you want to override it (y/n)? " o
    if [ $o != "y" ]; then
        echo "Exiting"
        exit 1
    fi
    rm $dbname
fi

echo $commands | sqlite3 $dbname