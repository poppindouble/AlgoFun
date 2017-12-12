"""
xor ^
two same number will get 0
so use origin array xor the one we have
the last number is what we need
"""

class Solution:
	def missingNumber(self, nums):
		result = 0
		for i in range(len(nums)):
			result = result ^ (i + 1) ^ nums[i]
		return result
def main():
	print(Solution().missingNumber([0, 1, 2, 3, 5, 6]))

if __name__ == "__main__":
	main()