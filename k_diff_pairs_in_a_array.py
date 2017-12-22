from collections import Counter
class Solution:
	def findPairs(self, nums, k):
		if k < 0:
			return 0
		myDict = Counter(nums)
		counter = 0
		for key, val in myDict.items():
			if k == 0:
				if val > 1:
					counter += 1
				continue
			if myDict[key + k]:
				counter += 1
		return counter


def main():
	print(Solution().findPairs([3, 1, 4, 1, 5], 2))

if __name__ == "__main__":
	main()