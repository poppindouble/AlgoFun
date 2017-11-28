class Solution:
	def isValid(self, s):

		dic = {
			'(' : ')',
			'[' : ']',
			'{' : '}'
		}

		myStack = []
		for char in s:
			if self.__isOpenParentheses__(char):
				myStack.append(char)
			else:
				if len(myStack) == 0:
					return False
				topElement = myStack.pop()
				if dic[topElement] != char:
					return False
		if len(myStack) != 0:
			return False
		return True


	def __isOpenParentheses__(self, char):
		if (char == '(' or char == '[' or char == '{'):
			return True
		else:
			return False

def main():
	print(Solution().isValid("()[]{}[{}]([]){[([])]}[}"))

if __name__ == "__main__":
	main()