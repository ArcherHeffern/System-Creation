from typing import NewType

Username = NewType("Username", str)
Password = NewType("Password", str)

# User database
users: dict[Username, Password] = {}

# Create dummy data
users["Timmy"] = "Timmy123"
users["Johnny"] = "1234"
users["Sarah"] = "snufalufagus"

def simple_auth(username: Username, password: str):
    return users[username] == password
    


# Requirements: 
# - Don't want to store passwords in our database
# - Don't want to have to send password on every request 

# Solution: Hashing



# HASH FUNCTION
# EG. Sha 256