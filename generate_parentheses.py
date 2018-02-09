class Solution:
	def __init__(self):
		self.res = []

	def generateParenthesis(self, n):
		self.__helper__(n, n, "")
		return self.res

	def __helper__(self, leftCount, rightCount, temp):

		if leftCount == 0 and rightCount == 0:
			self.res.append(temp)

		if rightCount < leftCount:
			return
			
		if leftCount > 0:
			self.__helper__(leftCount - 1, rightCount, temp + "(")
		if rightCount > 0:
			self.__helper__(leftCount, rightCount - 1, temp + ")")

		

def main():
	print(Solution().generateParenthesis(3))

if __name__ == "__main__":
	main()