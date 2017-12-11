class MyQueue:

	def __init__(self):
		self.stack = []

	def push(self, x):
		temp = []
		while self.stack:
			temp.append(self.stack.pop())
		temp.append(x)
		while temp:
			self.stack.append(temp.pop())

	def pop(self):
		return self.stack.pop()

	def peek(self):
		return self.stack[-1]

	def empty(self):
		return len(self.stack) == 0

def main():
	myQueue = MyQueue()
	myQueue.push(3)
	print(myQueue.peek())
	myQueue.push(5)
	print(myQueue.peek())
	print(myQueue.empty())
	myQueue.pop()
	print(myQueue.peek())

if __name__ == "__main__":
	main()