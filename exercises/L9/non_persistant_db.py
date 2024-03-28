#!/usr/bin/env python3

"""
TODO:
-- Improve Reservation Dataclass datatypes

Version 0.1.0 Ming Wang 
-- Github: https://github.com/MingCWang
-- Persistant CSV tabular DBMS
Version 0.2.0 Archer Heffern 
-- Removed Persistance
Version 0.3.0 Archer Heffern
-- Error handling, meta commands, and more database esq user flow
"""

from dataclasses import dataclass 
import dataclasses
import pprint

reservation_database: list['Reservation'] = []

RESERVATION_NOT_FOUND = "Reservation Not Found"
RESERVATIONS_NAME = "Reservations"

@dataclass
class Reservation:
    last_name: str
    phone_number: str
    reservation_date: str
    reservation_time: str
    party_size: int
    reservation_notes: str


def main():
    print("welcome to the reservation system!")
    print(".help to show help")

    while True:
        command = input("> ")
        tokens = command.split(" ")
        action = tokens[0].lower()

        if action == "":
            continue

        if action.startswith("."):
            handle_metacommand(action, tokens)
            continue

        match action:
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
            case "types":
                list_types()
            case _:
                print("Invalid command")


def print_help():
    print("""
       Commands:
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
        print("Usage: .schema <schema>")
        return
    schema = tokens[1]
    if schema == RESERVATIONS_NAME:
        print(f"__{RESERVATIONS_NAME}__\n{list_types()}")
    else:
        print(f"Schema {schema} not found")

def handle_metacommand(command, tokens):
    match command:
        case ".help":
            print_help()
        case ".exit":
            print("Exiting...")
            exit(0)
        case ".schema":
            if len(tokens) < 2:
                print("Usage: .schema <tablename>")
            print_schema(tokens)
        case ".tables":
            print_tables()
        case _:
            print("Metacommand not found")


def create(tokens: list[str]):
    if len(tokens) != 7:
        print("Creating a reservation requires 7 fields")
        return
    last_name = tokens[1]
    phone_number = tokens[2]
    reservation_date = tokens[3]
    reservation_time = tokens[4]
    party_size = tokens[5]
    reservation_notes = tokens[6]

    reservation = Reservation(
        last_name,
        phone_number,
        reservation_date, 
        reservation_time, 
        party_size,
        reservation_notes
    )
    reservation_database.append(reservation)


def select(last_name: str) -> int: 
    """
    Powerhouse function: Used for searching, deleting, and updating
    Can be updated to be way more expressive (search by phone_number, date, etc)
    Returns: Index of element in reservation_database
    """
    for i, reservation in enumerate(reservation_database):
        if reservation.last_name == last_name: 
            return i


def search(tokens: list[str]):
    if len(tokens) != 2:
        print("Usage: search last_name")
        return
    last_name = tokens[1]
    index: int = select(last_name)
    if index is None:
        print(RESERVATION_NOT_FOUND)
        return
    print(reservation_database[index])


def update(tokens: list[str]):
    """Returns the new Reservation or None if not found"""
    if len(tokens) != 4:
        print("Usage: update last_name type change")
        return
    last_name = tokens[1]
    field = tokens[2]
    change = tokens[3]

    index: int = select(last_name)
    if index is None:
        print(RESERVATION_NOT_FOUND)
        return
    # Does not check if is valid field
    setattr(reservation_database[index], field, change)

def list_types():
    return "\n".join([field.name for field in dataclasses.fields(Reservation)])

def cancel(tokens: list[str]):
    if len(tokens) != 2:
        print("Usage: CANCEL last_name")
        return
    last_name = tokens[1]
    index = select(last_name)
    if index is None:
        print(RESERVATION_NOT_FOUND)
        return
    reservation_database.pop(index)


def reservations():
    pprint.pprint(reservation_database)


main()
