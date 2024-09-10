from typing import Callable

class Test:
	def __init__(self):
		self.things = {}

	def route(self, path: str, method: str):
		def decorator(func: Callable):
			self.things[(path, method)] = func
		return decorator
	
	def get(self, path: str):
		return self.route(path, "GET")

	def put(self, path: str):
		return self.route(path, "PUT")

	def post(self, path: str):
		return self.route(path, "POST")

	def patch(self, path: str):
		return self.route(path, "PATCH")

	def delete(self, path: str):
		return self.route(path, "DELETE")

if __name__ == '__main__':
	test = Test()
	@test.get("/usr/lib")
	def hello():
		print("Hello world")
	print(test.things)
		
