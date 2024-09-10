from typing import NewType

Username = NewType("Username", str)
Password = NewType("Password", str)

# User database
users: dict[Username, Password] = {}

# Create dummy data
users["Timmy"] = "Timmy123"
users["Johnny"] = "1234"
users["Sarah"] = "snufalufagus"

def simple_create_account(username: Username, password: Password) -> bool:
    if username in users:
        return False
    users[username] = password
    return True

def simple_login(username: Username, password: Password) -> bool:
    return users[username] == password

def simple_authenticate_request(username: Username, password: Password) -> bool:
    return simple_login(username, password)



# Using Tokens
import datetime
import random

Token = NewType("Token", str)
tokens: dict[Username, tuple[Token, datetime.datetime]] = {}

def simple_create_account(username: Username, password: Password) -> bool:
    if username in users:
        return False
    users[username] = password
    return True

def simple_token_login(username: Username, password: Password) -> Token:
    if users[username] == password:
        expire_date = datetime.datetime.today() + datetime.timedelta(days=90)
        token = random.randint(0, 10000)
        tokens[username] = (token, expire_date)
        
def simple_token_authenticate_request(username: Username, token: Token) -> bool:
    token_date_pair = tokens.get(username)
    if token_date_pair is None:
        return False
    if token_date_pair[0] != token:
        return False
    if token_date_pair[1] < datetime.datetime.today():
        return False
    return True

def revoke_token(username: Username):
    if username in tokens: 
        tokens.pop(username)

# HASH FUNCTION
# EG. Sha 256
