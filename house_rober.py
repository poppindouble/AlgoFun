"""
let's consider this question in this way:
let's assume a[i] is the solution for array nums ends at i th position
so:
a[0] = nums[0]
a[1] = max(nums[0], nums[1])
a[2] = max(nums[0] + nums[2], nums[1])
a[3] = max(nums[0] + nums[3], nums[1] + nums[3], nums[0] + nums[2])
.
.
etc

let's consider a[i]
only two scenario:
1. nums[i] is not included in a[i]
2. nums[i] is included in the a[i]

if nums[i] is not included in a[i], which means
a[i] = a[i - 1]
for example:

-----------------
a[2] = nums[1]
then
a[1] = nums[1]
because in a[2], we have
nums[0] + nums[2] < nums[1]
so in a[1], for sure we have
nums[0] < nums[1]
so
a[1] = nums[1]
------------------

a[3] = nums[0] + nums[2]
then
a[2] = nums[0] + nums[2]
because in a[3], we have
nums[0] + nums[2] > nums[0] + nums[3]
nums[0] + nums[2] > nums[1] + nums[3]
so in a[2], for sure we have
nums[0] + nums[2] > nums[1]
so
a[2] = nums[0] + nums[2]
------------------

which means:
for senario 1:
if nums[i] is not included in a[i]
then a[i] = a[i - 1]

for senario 2:
really easy to understand
if nums[i] is included in the a[i]
then the solution will be
a[i - 2] + nums[i]

after all:
a[i] = max(a[i - 1], a[i - 2] + nums[i])
"""

class Solution():
	# def rob(self, nums):
	# 	if not nums:
	# 		return 0
	# 	if len(nums) == 1:
	# 		return nums[0]
	# 	if len(nums) == 2:
	# 		return max(nums[0], nums[1])

	# 	m = nums[0]
	# 	n = max(nums[0], nums[1])
	# 	record = []
	# 	for i in nums[2:]:
	# 		result = max(n, m + i)
	# 		if result == m + i:
	# 			record.append(i)
	# 		m = n
	# 		n = result
	# 	print(record)
	# 	return result

	def rob(self, nums):
		if not nums:
			return 0
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return max(nums[0], nums[1])

		m = nums[0]
		n = max(nums[0], nums[1])
		for i in nums[2:]:
			if m == n:
				result = m + i
			else:
				result = n
			m = n
			n = result
		return result

def main():
	print(Solution().rob([4, 2, 5, 1, 9, 2, 6, 3, 1]))

if __name__ == "__main__":
	main()