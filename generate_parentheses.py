class Solution:
	# def __init__(self):
	# 	self.res = []

	# def generateParenthesis(self, n):
	# 	if n == 0:
	# 		return [""]
	# 	self.__helper__(n, n, "")
	# 	return self.res

	# def __helper__(self, leftCount, rightCount, temp):

	# 	if leftCount == 0 and rightCount == 0:
	# 		self.res.append(temp)

	# 	if rightCount < leftCount:
	# 		return
			
	# 	if rightCount > 0:
	# 		self.__helper__(leftCount, rightCount - 1, temp + ")")
	# 	if leftCount > 0:
	# 		self.__helper__(leftCount - 1, rightCount, temp + "(")


###################################################################################
	# def generateParenthesis(self, n):
	# 	res = self.dfs(n, n, "", [])
	# 	return res

	# def dfs(self, left, right, str, res):
	# 	print(left, right, str, res)

	# 	if left == right == 0:
	# 		res.append(str)
	# 		return res[:]
	# 	resLeft, resRight = [], []
	# 	if left > 0:
	# 		resLeft = self.dfs(left - 1, right, str + '(', res[:])
	# 		print("after left", resLeft, resRight, left, right)
	# 	if right > 0 and left < right:
	# 		resRight = self.dfs(left, right - 1, str + ')', res[:])
	# 		print("after right", resLeft, resRight, left, right)
	# 	return resRight + resLeft
###################################################################################

	def generateParenthesis(self, n):
		res = self.dfs(n, n)
		return res

	def dfs(self, left, right):
		if left == 0 and right == 1:
			return [")"]
		res = []
		if left > 0:
			temp = self.dfs(left - 1, right)
			res += list(map(lambda x: "(" + x, temp))
		if right > 0 and left < right:
			temp = self.dfs(left, right - 1)
			res += list(map(lambda x: ")" + x, temp))
		return res

def main():
	print(Solution().generateParenthesis(3))

if __name__ == "__main__":
	main()