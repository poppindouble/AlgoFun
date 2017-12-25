import sys

class Solution:
	def findMaxAverage(self, nums, k):
		result = 0
		temp = 0
		for index, num in enumerate(nums):
			if index < k:
				temp += num
				result += num
				continue
			temp = temp - nums[index - k] + num
			result = max(result, temp)
		return result / k

def main():
	print(Solution().findMaxAverage([0, 4, 0, 3, 2], 1))

if __name__ == "__main__":
	main()