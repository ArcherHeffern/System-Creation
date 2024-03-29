# Author: Ming Wang 
# Github: https://github.com/MingCWang

# TODO: Change such that csv file is not fully rewritten when modifying 

import csv
from os import access, R_OK, W_OK
from dataclasses import dataclass, fields
from pathlib import Path

@dataclass
class Reservation:
    last_name: str
    phone_number: str
    reservation_date: str
    reservation_time: str
    party_size: int
    reservation_notes: str

number_of_reservations = 0
RESERVATIONS_NAME = "Reservations"
EXT_ERR_BAD_PERMISSIONS = 1
FIELD_NAMES = [field.name for field in fields(Reservation)]
FILE = Path("reservations.csv")

write_header = False

if FILE.is_file():
    if not access(FILE, W_OK) or not access(FILE, R_OK):
        print("File exists but does not have correct permissions")
        exit(EXT_ERR_BAD_PERMISSIONS)
    with open(FILE) as f:
        reader = csv.DictReader(f)
        for line in reader:
            number_of_reservations += 1
else:
    with open(FILE, "w") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
    
    

def print_help():
    print("""Commands:
        CREATE <field1 ...>                 Create a new reservation.
        SEARCH <name>      	      	        Search reservation by last name.
        UPDATE <name> <type> <change> 	    Update reservation by last name.
        CANCEL <name>          	 	        Cancel reservation by last name.
        RESERVATIONS                  		List all active reservations.
        .help                               Show this list of commands.
        .exit                          	    Close this program and save updates.
        .schema <tablename>                 Shows schema for a table.
        .tables                             Lists names of all tables.
       """)

def print_tables():
    print(RESERVATIONS_NAME)

def print_schema(tokens):
    if len(tokens) != 2:
        print("Schema not specified")
        return
    schema = tokens[1]
    if schema == RESERVATIONS_NAME:
        combined = "\n".join(FIELD_NAMES)
        print(f"__{RESERVATIONS_NAME}__\n{combined}")
    else:
        print("Schema not found")

def handle_metacommand(command, tokens):
    match command:
        case ".help":
            print_help()
        case ".exit":
            print("Exiting...")
            exit(0)
        case ".schema":
            print_schema(tokens)
        case ".tables":
            print_tables()
        case _:
            print("Metacommand not found")


def main():
    print("welcome to the reservation system!")
    print(".help to show help")

    while True:
        tokens = input("> ").split()
        command = tokens[0]
        if command == "":
            continue

        if command.startswith("."):
            handle_metacommand(command, tokens)
            continue

        match command:
            case "create":
                create(tokens)
            case "search":
                search(tokens)
            case "update":
                update(tokens)
            case "cancel":
                cancel(tokens)
            case "reservations":
                reservations()
            case _:
                print("Invalid command")

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


def create(tokens: list[str]):
    if len(tokens) != 7:
        print("CREATE Invalid Datatype Syntax")
        return
    last_name = tokens[1]
    phone_number = tokens[2]
    reservation_date = tokens[3]
    reservation_time = tokens[4]
    party_size = tokens[5]
    reservation_notes = tokens[6]

    global number_of_reservations

    number_of_reservations += 1

    with open("reservations.csv", "a") as file:
        writer_object = csv.DictWriter(file, fieldnames=FIELD_NAMES)

        writer_object.writerow(
            {
                "last_name": last_name,
                "phone_number": phone_number,
                "reservation_date": reservation_date,
                "reservation_time": reservation_time,
                "party_size": party_size,
                "reservation_notes": reservation_notes,
            }
        )


def search(tokens):
    last_name = tokens[1]
    with open("reservations.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Guest Name"] == last_name:
                print(row)


def update(tokens):
    if len(tokens) < 4:
        print("Not enough arguments for update")
    last_name = tokens[1]
    type = tokens[2]
    change = tokens[3]

    if type not in FIELD_NAMES:
        print("Invalid type")
        return

    with open("reservations.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row["Guest Name"] == last_name:
            row[type] = change

    with open("reservations.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(rows)


def cancel(command):
    last_name = command.split(" ")[1]
    with open("reservations.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row["Guest Name"] == last_name:
            rows.remove(row)

    with open("reservations.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, FIELD_NAMES)
        writer.writeheader()
        writer.writerows(rows)


def reservations():
    with open("reservations.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


main()
