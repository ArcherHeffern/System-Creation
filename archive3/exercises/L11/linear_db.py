
data = []

def main():
    while (True):
        commands = input().split()
        if len(commands) == 0:
            continue
        command = commands[0]
        if command == "CREATE":
            create(commands)

def create(data):
    # Serialize the data
    if data
