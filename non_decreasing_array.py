class Solution:
	def checkPossibility(self, nums):
		i, j = 0, 1
		counter = 1
		while j < len(nums):
			if nums[j] < nums[i]:
				if counter == 0:
					return False
				if j == len(nums) - 1:
					return True
				if nums[j + 1] >= nums[i]:
					counter -= 1
				elif i == 0 or nums[i - 1] <= nums[j]:
					counter -= 1
				else:
					return False
			i += 1
			j += 1
		return True


def main():
	print(Solution().checkPossibility([-1, 4, 2, 3]))

if __name__ == "__main__":
	main()