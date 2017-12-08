class MinStack:

	def __init__(self):
		self.stack = []
		self.minStack = []

	def push(self, x):
		self.stack.append(x)
		if not self.minStack:
			self.minStack.append(x)
		elif self.minStack[-1] >= x:
			self.minStack.append(x)

	def pop(self):
		last = self.stack.pop()
		if last == self.minStack[-1]:
			self.minStack.pop()
		return last

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.minStack[-1]

def main():
	myStack = MinStack()
	myStack.push(-2)
	myStack.push(0)
	myStack.push(-3)
	myStack.getMin()
	myStack.pop()
	myStack.pop()
	myStack.getMin()

if __name__ == "__main__":
	main()