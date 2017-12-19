class Solution:
	def findMaxConsecutiveOnes(self, nums):
		result = 0
		i = j = 0
		while j < len(nums):
			if nums[j] == 1:
				j += 1
				continue
			result = max(result, j - i)
			j += 1
			i = j
		return max(result, j - i)

def main():
	print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1]))

if __name__ == "__main__":
	main()