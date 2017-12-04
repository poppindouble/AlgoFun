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

"""

class Solution:
	def maxSubArray(self, nums):
		m, result = nums[0], nums[0]

		for i in range(1, len(nums)):
			m = max(m + nums[i], nums[i])
			if m > result:
				result = m
		return result

def main():
	print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == "__main__":
	main()