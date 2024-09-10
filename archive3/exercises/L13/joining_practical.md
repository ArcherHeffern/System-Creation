## get_chat_room
Define a function called get_chat_room. It should return all the data we want to see when navigating to a chat room. 

```python
db = ...

def get_chat_room(chat_room_id):
    """Returns all chat room name and all messages"""
    db.execute("SELECT name FROM ChatRoom WHERE chatroom_id=%s" % chatroom_id)



```