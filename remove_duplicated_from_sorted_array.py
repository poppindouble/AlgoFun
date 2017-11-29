class Solution:
	def removeDuplicates(self, nums):
		if len(nums) < 2:
			return len(nums)

		i, j = 0, 0

		while j < len(nums):
			if nums[i] == nums[j]:
				j += 1
				continue
			else:
				i += 1
				nums[i] = nums[j]

		return nums


def main():
	print(Solution().removeDuplicates([1,2,3,4,5,6,7,8,9,10]))

if __name__ == "__main__":
	main()