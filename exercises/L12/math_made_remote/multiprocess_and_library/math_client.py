from remote_math_lib import RemoteMathLib

def handle(p_read: int, p_write: int):
    math = RemoteMathLib(p_read, p_write)
    print(math.ceil(5.5))
    print(math.floor(5.5))
