"""
This is a classic dynamic programming question.
Let's see the traditional solution:
Use M[i] represent the maximum subarry which HAVE TO INCLUDE nums[i] AS THE LAST ELEMENT

so,
M[0] = nums[0]
M[1] = max(nums[0] + nums[1], nums[1]), because we have to include nums[1], so only two possible value, nums[0] + nums[1] or nums[1]
which is also max(M[0] + nums[1], nums[1])
M[1] = max(M[0] + nums[1], nums[1])
M[2] = max(nums[0] + nums[1] + nums[2], nums[1] + nums[2], nums[2]), which again max(nums[0] + nums[1] + nums[2], nums[1] + nums[2]) is
max(M[1] + nums[2])
M[2] = max(M[1] + nums[2], nums[2])
.
.
.
M[i] = max(M[i - 1] + nums[i], nums[i])
At the end, we just need to find max(M[1], M[2], M[3] ...)

--------------------------

There is another thinking:
keep two pointer, and one temp variable
i start from 0
j start from 1
temp = nums[0]
max = nums[0]

if temp < 0, we set i = j
update max with the current temp
then reset the temp as nums[i]
j move forward

else, we update the temp with temp + nums[j]
move j forward,

The thinking is like this:
i is the start point of the maximum subarray
temp represent the sum of the subarray start at i
if temp is > 0, which means, we might still have a chacne that next
value will be positive, so the maximum subarray might still start from i
But, if at some point, the temp become < 0, then we need to update
our i to j, get rid of the negative subarray

"""

class Solution:
	# def maxSubArray(self, nums):
	# 	m, result = nums[0], nums[0]

	# 	for i in range(1, len(nums)):
	# 		m = max(m + nums[i], nums[i])
	# 		if m > result:
	# 			result = m
	# 	return result

	def maxSubArray(self, nums):
		i, j = 0, 1
		temp = nums[0]
		result = nums[0]

		while j <= len(nums):
			if j == len(nums):
				return max(result, temp)
			if temp < 0:
				i = j
				temp = nums[i]
				j += 1
			else:
				temp = temp + nums[j]
				j += 1

			result = max(result, temp)



def main():
	print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
	main()