class Solution:
	def findRelativeRanks(self, nums):
		newNums = sorted(nums, reverse=True)
		medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		myDict = {}
		for index, num in enumerate(newNums):
			if index < 3:
				myDict[num] = medals[index]
				continue
			myDict[num] = str(index + 1)
		return list(map(lambda x: myDict[x], nums))

def main():
	print(Solution().findRelativeRanks([5, 8, 1, 3, 9]))

if __name__ == "__main__":
	main()