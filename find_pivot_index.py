class Solution:
	def pivotIndex(self, nums):
		if len(nums) == 0:
			return -1
		if len(nums) == 1:
			return 0
		leftSum = 0
		rightSum = sum(nums)
		i = 0
		while i < len(nums):
			rightSum -= nums[i]
			if leftSum == rightSum:
				return i
			leftSum += nums[i]
			i += 1
		return -1

def main():
	print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))

if __name__ == "__main__":
	main()