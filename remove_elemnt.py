class Solution:
	def removeElement(self, nums, val):
		if not nums:
			return 0

		i, j = 0, 0

		while j < len(nums):
			if nums[j] == val:
				j += 1
				continue
			else:
				nums[i] = nums[j]
				i += 1
				j += 1

		return i

def main():
	print(Solution().removeElement([3,2,2,3], 3))

if __name__ == "__main__":
	main()