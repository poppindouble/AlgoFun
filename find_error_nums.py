class Solution:
	def findErrorNums(self, nums):
		first = second = None
		for num in nums:
			num = abs(num)
			if nums[num - 1] < 0:
				first = num
			nums[num - 1] = -abs(nums[num - 1])
		for index, num in enumerate(nums):
			if num > 0:
				second = index + 1
		return [first, second]
		

def main():
	print(Solution().findErrorNums([3,2,2]))

if __name__ == "__main__":
	main()