class Solution:
	# def findDisappearedNumbers(self, nums):
	# 	result = []
	# 	mySet = set(nums)
	# 	for i in range(1, len(nums) + 1):
	# 		if i not in mySet:
	# 			result.append(i)
	# 	return result

	def findDisappearedNumbers(self, nums):
		for n in nums:
			nums[abs(n) - 1] = -abs(nums[abs(n) - 1])

		print([index for index in range(0,len(nums)) if nums[index] > 0])

def main():
	print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))

if __name__ == "__main__":
	main()