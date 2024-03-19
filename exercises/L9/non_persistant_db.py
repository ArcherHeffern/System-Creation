#!/usr/bin/env python3

"""
TODO:
-- Error handling
-- Improve Reservation Dataclass datatypes

Version 0.1.0 Ming Wang 
-- Github: https://github.com/MingCWang
-- Persistant CSV tabular DBMS
Version 0.2.0 Archer Heffern 
-- Removed Persistance
"""

from dataclasses import dataclass 
import dataclasses
import pprint

reservation_database: list['Reservation'] = []

RESERVATION_NOT_FOUND = "Reservation Not Found"

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
    cmds = """
       Usage:  
         execute <command> [options]


       Commands:
         create                     	    	Create a new reservation.
         search <last name>          	      	Search reservation by last name.
         update <last name> <type> <change> 	Update reservation by last name.
         cancel <last name>          	 	Cancel reservation by last name.
         reservations                  		List all active reservations.
         types                              List types used in update.
         help                          		Show this list of commands.
         exit                          		Close this program and save updates.
      
       """

    print(cmds)
    while True:
        command = input("Enter a command: ")
        tokens = command.split(" ")
        action = tokens[0]
        if action == "create":
            create()
        elif action == "search":
            search(tokens)
        elif action == "update":
            update(tokens)
        elif action == "cancel":
            cancel(tokens)
        elif action == "reservations":
            reservations()
        elif action == "types":
            list_types()
        elif action == "help":
            print(cmds)
        elif action == "exit":
            break
        else:
            print("Invalid command")

        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("Changes saved, thank you for using the reservation system!")


def create():
    last_name = input("Enter last name (string: Any): ")
    phone_number = input("Enter phone number (string: xxx-xxx-xxxx): ")
    reservation_date = input("Enter reservation date (string: yyyy-mm-dd): ")
    reservation_time = input("Enter reservation time (string: hh-mm): ")
    party_size = input("Enter party size (integer: Any): ")
    reservation_notes = input("Enter reservation notes (string: Any): ")

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
    print("\t".join([field.name for field in dataclasses.fields(Reservation)]))

def cancel(tokens: list[str]):
    if len(tokens) != 2:
        print("Usage: cancel last_name")
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
