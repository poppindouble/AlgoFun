class Solution:
	def moveZeros(self, nums):
		i = 0
		for j in range(len(nums)):
			if nums[j] == 0:
				continue
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
		print(nums)

def main():
	Solution().moveZeros([0, 3, 1, 0, 2, 0, 0, 3, 12])

if __name__ == "__main__":
	main()