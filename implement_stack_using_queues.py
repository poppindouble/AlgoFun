class MyStack:
	def __init__(self):
		self.queue = []

	def push(self, x):
		self.queue.append(x)
		for i in range(len(self.queue) - 1):
			self.queue.append(self.queue.pop(0))

	def pop(self):
		if not self.empty():
			return self.queue.pop(0)
		else:
			return

	def top(self):
		if not self.empty():
			return self.queue[0]
		else:
			return

	def empty(self):
		return len(self.queue) == 0

def main():
	myStack = MyStack()
	myStack.push(3)
	myStack.push(4)
	print(myStack.queue)
	print(myStack.pop())
	print(myStack.top())
	print(myStack.empty())

if __name__ == "__main__":
	main()