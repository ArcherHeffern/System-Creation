from sock_util import *
from remote_math_lib import RemoteMathLib
import signal

def main():
	signal.signal(signal.SIGINT, lambda *x: exit(0))

	print("`help` for a help menu")
	math = RemoteMathLib()
	while True:
		# User Interface
		tokens = input("> ").split()
		if len(tokens) == 0:
			continue
		command = tokens[0]
		match command:
			case "exit"|"q"|"quit":
				break
		if len(tokens) < 2:
			print("Not enough arguments")
			continue
		val = tokens[1]
		match command:
			case "floor":
				val = math.floor(val)
			case "ceil":
				val = math.ceil(val)
			case "cos":
				val = math.cos(val)
			case "sin":
				val = math.sin(val)
			case default:
				val = "Invalid Command"
		print(val)

	print("Exiting...")

if __name__ == '__main__':
	main()
