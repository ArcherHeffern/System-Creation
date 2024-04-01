import sqlite3

DBNAME = "Chat"
PROMPT = "> "

CON = None

# Lesson 1: Feature specifications and Design database tables
# Lesson 2: Code some database tables and make implement simple features: Join group chat, list group chats
# Lesson 3: Querying through keys using Joins and Authentication

def main():
    initialize_database()
    while True:
        command, tokens = parse_input()
        if command == "":
            continue
        match command: 
            case "create_account":
                create_account(tokens)
            case "login":
                login(tokens)
            case "list_group_chat":
                list_group_chat(tokens)
            case "get_group_chat":
                get_group_chat(tokens)
            case "send_chat":
                send_chat(tokens)

def create_account(tokens):
    ...

def login(tokens):
    ...

def send_chat(tokens):
    ...

def list_group_chat(tokens):
    ...

def join_group_chat(tokens):
    ...

def leave_group_chat(tokens):
    ...
            
def get_group_chat(tokens):
    # TODO
    """
    - get group chat name
    - 
    - get all notifications 
    """
    ...

def parse_input() -> tuple[str, list[str]]:
    tokens = input(PROMPT).split()
    return tokens[0], tokens

def initialize_database(dummy_data: bool = False, clean: bool = True):
    CON = sqlite3.connect(DBNAME)
    cur = CON.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS User (user_id int primary key, username varchar(20), email varchar(20), password varchar(20), timestamp text);")
    cur.execute("CREATE TABLE IF NOT EXISTS ChatRoom (chatroom_id int primary key, name varchar(20), timestamp text);")
    cur.execute("CREATE TABLE IF NOT EXISTS ChatRoomUserJunctionTable (chatroom_user_id int primary key, member int, chatroom int, FOREIGN KEY(member) REFERENCES User(user_id), FOREIGN KEY(chatroom) REFERENCES ChatRoom(chatroom_id));")
    cur.execute("CREATE TABLE IF NOT EXISTS Message (message_id int primary key, sender int, chatrooom_id int, timestamp text, edited int, FOREIGN KEY(sender) REFERENCES User(user_id), FOREIGN KEY(chatroom_id) REFERENCES ChatRoom(chatroom_id)));")
    cur.execute("CREATE TABLE Notification (notification_id int primary key, message_id int, user_id int, seen int, notification_type text, timestamp text, FOREIGN KEY(message_id) REFERENCES Message(message_id), FOREIGN KEY(user_id) REFERENCES User(user_id));")
    if clean:
        for table in ["User", "ChatRoom", "ChatRoomUserJunctionTable", "Message", "Notification"]:
            cur.execute("TRUNCATE TABLE ?;", table)
        
    if dummy_data:
        chatroom_data = [
            ("Cool kids", "10/10"),
            ("Cooler kids", "6/4")
        ]
        cur.executemany("INSERT INTO ChatRoom VALUES (?, ?);", chatroom_data)
        chat_room_user_data = [
            (0, 0),
            (0, 1),
            (1, 0),
            (2, 2),
            (1, 2)
        ]
        cur.executemany("INSERT INTO ChatRoomUserJunctionTable VALUES (?, ?);", chat_room_user_data)


        user_data = [
            ("Timmy", "TimmyTurner@gmail.com", "timmyrox", "10/27"),
            ("Steven", "stvn@gmail.com", "steveiscool", "1/23"),
            ("Sarah", "hilly@ihop.com", "12354", "5/93")
                    ]
        cur.executemany("INSERT INTO User VALUES (?, ?);", user_data)

        # TODO: Other tables dummy data


main()