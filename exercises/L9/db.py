# Author: Ming Wang 
# Github: https://github.com/MingCWang
import csv

number_of_reservations = 0

with open("reservations.csv", "rx") as file:
    reader = csv.reader(file)
    for row in reader:
        number_of_reservations = len(list(reader))


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
         help                          		Show this list of commands.
         exit                          		Close this program and save updates.
      
       """

    print(cmds)
    exit = True
    while exit:
        command = input("Enter a command: ")
        action = command.split(" ")[0]
        if action == "create":
            create()
        elif action == "search":
            search(command)
        elif action == "update":
            update(command)
        elif action == "cancel":
            cancel(command)
        elif action == "reservations":
            reservations()
        elif action == "help":
            print(cmds)
        elif action == "exit":
            exit = False
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

    global number_of_reservations

    number_of_reservations += 1

    with open("reservations.csv", "a") as file:
        writer_object = csv.writer(file)

        writer_object.writerow(
            [
                number_of_reservations,
                last_name,
                phone_number,
                reservation_date,
                reservation_time,
                party_size,
                reservation_notes,
            ]
        )


def search(command):
    last_name = command.split(" ")[1]
    with open("reservations.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Guest Name"] == last_name:
                print(row)


def update(command):
    last_name = command.split(" ")[1]
    type = command.split(" ")[2]
    change = command.split(" ")[3]
    typeDict = {
        "name": "Guest Name",
        "phone": "Guest Phone",
        "date": "Date",
        "time": "Time",
        "size": "Size",
        "notes": "Notes",
    }

    if type in typeDict:
        type = typeDict[type]

    with open("reservations.csv", "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row["Guest Name"] == last_name:
            row[type] = change

    with open("reservations.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
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
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def reservations():
    with open("reservations.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


main()
