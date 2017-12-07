class Solution:
	def singleNumber(self, nums):
		result = nums[0]
		for num in nums[1:]:
			result = result ^ num
		return result

def main():
	print(Solution().singleNumber([1, 2, 1, 2, 4, 99, 4]))

if __name__ == "__main__":
	main()