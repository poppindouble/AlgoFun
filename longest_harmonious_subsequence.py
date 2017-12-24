from collections import Counter
class Solution:
	def findLHS(self, nums):
		myDict = Counter(nums)
		result = 0
		for key, val in myDict.items():
			if key + 1 in myDict:
				result = max(result, myDict[key] + myDict[key + 1])
		return result

def main():
	print(Solution().findLHS([1,3,2,2,5,2,3,7]))

if __name__ == "__main__":
	main()