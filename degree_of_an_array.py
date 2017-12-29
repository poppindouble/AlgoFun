class Solution():
	"""
	brute force
	"""
	def findShortestSubArray(self, nums):
		myDict = {}
		miniIndex = {}
		maxIndex = {}
		result = len(nums)
		degrees = -1
		for index, num in enumerate(nums):
			if num in myDict:
				myDict[num] += 1
			else:
				myDict[num] = 1
				miniIndex[num] = index
			maxIndex[num] = index
			degrees = max(degrees, myDict[num])
		for num in nums:
			if myDict[num] == degrees:
				result = min(result, maxIndex[num] - miniIndex[num] + 1)
		return result
		

def main():
	print(Solution().findShortestSubArray([1, 2, 2, 3, 1]))

if __name__ == "__main__":
	main()