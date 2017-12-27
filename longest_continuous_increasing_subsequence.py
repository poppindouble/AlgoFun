class Solution:
	def findLengthOfLCIS(self, nums):
		result = -1
		if len(nums) <= 1:
			return len(nums)
		i, j = 0, 1
		counter = 1
		while j < len(nums):
			if nums[i] < nums[j]:
				counter += 1
			else:
				result = max(result, counter)
				counter = 1
			i += 1
			j += 1
		return max(result, counter)

def main():
	print(Solution().findLengthOfLCIS([3,4,5,2,12,3,4,5,6,7,8]))

if __name__ == "__main__":
	main()