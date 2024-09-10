"""
Example of Parser and Command Modules: Not complete - Just for theory
Parser: For reading
Command Module: For sending
"""
# Application 1 - Single Process Client with a Command Module and a Parse Module
# Note: A Client at minimum is a command module - It might not have parse module if its not reading server response
from socket import Socket
from commandCreator import CommandCreator # type: ignore
from commandSender import CommandSender # type: ignore
from responseHandler import ResponseHandler #type: ignore

socket = Socket.connect("127.0.0.1", 8080)

commandCreator = CommandCreator()
commandSender = CommandSender(socket)
responseHandler = ResponseHandler()

while True:
	command, tokens = input("> ").split(maxsplit=1)
	cmd = commandCreator(command, tokens) # Returns str formatted as JSON "{cmd: "send", msg: "<msg>"}
	...
	response: str = commandSender.send(cmd) # Returns remote machine response as string
	responseHandler.handle(response)
	
# Application 2 - Forking Server with Command module and Parse Module 
# Note: A Server at minimum has a Parse Module - It might not have command module because its not sending commands to remote
from socketServer import SocketServer
from commandReceiver import CommandReceiver
from commandParser import CommandParser
from commandExecutor import CommandExecutor
from responseSender import ResponseSender

socketserver = SocketServer("127.0.0.1", 8080)

while True:
	connection = socketserver.accept()
	if fork() != 0:
		connection.close()
		continue
	commandReceiver = CommandReceiver(connection)
	commandParser = CommandParser()
	commandExecutor = CommandExecutor()
	responseSender = ResponseSender(connection)

	while True:
		command: str = commandReceiver.receive()
		parsed_command: Command|None = commandParser.parse(command)
		if parsed_command is None:
			continue
		response: Response = commandExecutor.execute(parsed_command)
		responseSender.send(response)
	


