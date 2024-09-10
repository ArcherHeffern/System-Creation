#!/usr/bin/env python3

import sqlite3
connection = sqlite3.connect("Students")
cursor = sqlite3.Cursor(connection)
command = """CREATE TABLE students (
    name int,
    age varchar(255),
    height int
);
"""
cursor.execute(command)
