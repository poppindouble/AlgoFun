"""
if the majority element is more then ⌊ n/2 ⌋ times
it means, the quantity of this element is always at least 1 more then
the quantity of the rest elements
"""


class Solution():
	def majorityElement(self, nums):
		if len(nums) == 1:
			return nums[0]
		majority = nums[0]
		counter = 1
		for i in nums[1:]:
			counter = counter + 1 if majority == i else counter - 1
			if counter < 0:
				majority = i
				counter = 1
		return majority

def main():
	print(Solution().majorityElement([2,2,2,2,2,4,4,4,4,4,4]))

if __name__ == "__main__":
	main()