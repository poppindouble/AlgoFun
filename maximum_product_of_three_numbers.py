class Solution:
	def maximumProduct(self, nums):
		[first, second, third] = sorted(nums[0:3])[::-1]
		smallest, secondSmallest = third, second
		for num in nums[3:]:
			if num <= smallest:
				smallest, secondSmallest = num, smallest
			elif num <= secondSmallest:
				secondSmallest = num

			if num >= first:
				first, second, third = num, first, second
			elif num >= second:
				second, third = num, second
			elif num >= third:
				third = num
		return first * second * third

def main():
	print(Solution().maximumProduct([9,5,7,2,3,10,4]))

if __name__ == "__main__":
	main()