from os import read, write
from math_server import NOT_ENOUGH_ARGUMENTS, UNKNOWN_COMMAND, VALUE_ERROR

"""
This is convenient because we don't need to have to know the network protocol and it handles all the connection and IPC logic for us. This is especially important for more complex protocols 

While I did not do this, connect, floor, ceil, etc, would also make sense as functions which will take a connection struct as an argument. This is up to you. 

"""

class RemoteMathLib:
    def __init__(self, read_fd: int, write_fd: int):
        self.__read_fd = read_fd
        self.__write_fd = write_fd

    def __handle__(self, command: str, *values) -> int:
        msg = command + " "
        for value in values:
            msg += str(value) + " "
        write(self.__write_fd, msg.encode())
        result = read(self.__read_fd, 128).decode()
        if result.startswith("success:"):
            return int(result.removeprefix("success:"))
        raise Exception(result)
        

    def floor(self, x: int):
        return self.__handle__("floor", x)

    def ceil(self, x: int):
        return self.__handle__("ceil", x)

    def cos(self, x: int):
        return self.__handle__("cos", x)

    def sin(self, x: int):
        return self.__handle__("sin", x)