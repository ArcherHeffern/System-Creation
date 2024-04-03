from os import write, read

def handle(p_read, p_write):
    print("`help` for a help menu")
    while True:
        user_input = input("> ")
        if user_input == "exit":
            break
        write(p_write, user_input.encode())
        remote_result = read(p_read, 1024).decode()
        print(f"Remote: {remote_result}")
    print("Exiting...")