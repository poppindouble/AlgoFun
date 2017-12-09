"""
the best solution is using O(1) space complexity
if we use 
nums[:] = nums[len(nums)-k:] + nums[0:len(nums)-k]
then we are using n extra space complexity.
one thing to notice is that
if we do
nums = nums[len(nums)-k:] + nums[0:len(nums)-k]
it is creating a new variable call nums, not changing the origin one

ref:
https://www.python-course.eu/passing_arguments.php
https://www.python-course.eu/deep_copy.php
https://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm

so, if we want in place change, we can't use index slicing, cuz it will copy a new one

when we pass an array using
nums[:] or nums[1:5]
it is making a copy


let's considert this solution:
[1, 2, 3, 4, 5, 6, 7], k = 3
let's reverse both side [1, 2, 3, 4] and [5, 6, 7]
we get
[4, 3, 2, 1] and [7, 6, 5]
then we reverse it again
[5, 6, 7, 1, 2, 3, 4]
"""

class Solution():
	def rotate(self, nums, k):
		self.__reverse__(nums, 0, len(nums) - k)
		self.__reverse__(nums, len(nums) - k, len(nums))
		self.__reverse__(nums, 0, len(nums))
		print(nums)

	def __reverse__(self, nums, start, end):
		middle = (start + end) // 2
		for i in range(start, middle):
			nums[i], nums[start + end - 1 - i] = nums[start + end - 1 - i], nums[i]


def main():
	Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)

if __name__ == "__main__":
	main()