class Solution:
	def calPoints(self, ops):
		myStack = []
		for op in ops:
			if op == 'C':
				myStack.pop()
			elif op == 'D':
				last = myStack[-1]
				last = last * 2
				myStack.append(last)
			elif op == '+':
				last = myStack.pop()
				second = myStack.pop()
				temp = last + second
				myStack.append(second)
				myStack.append(last)
				myStack.append(temp)
			else:
				myStack.append(int(op))
		return sum(myStack)

def main():
	print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))

if __name__ == "__main__":
	main()