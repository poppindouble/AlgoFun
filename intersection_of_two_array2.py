"""
let's do another solution, let's assume time is not important
so we can sort the array

also pay attention how we use counter
"""
from collections import Counter

class Solution:
	def intersect(self, nums1, nums2):
		myDict = Counter(nums1)
		result = []
		for num in nums2:
			if num in myDict and myDict[num] != 0:
				result.append(num)
				myDict[num] -= 1
		return result


	# def intersect(self, nums1, nums2):
	# 	nums1 = sorted(nums1)
	# 	nums2 = sorted(nums2)
	# 	i, j = 0, 0
	# 	result = []

	# 	while i < len(nums1) and j < len(nums2):
	# 		if nums1[i] > nums2[j]:
	# 			j += 1
	# 		if nums1[i] < nums2[j]:
	# 			i += 1
	# 		if nums1[i] == nums2[j]:
	# 			result.append(nums1[i])
	# 			i += 1
	# 			j += 1
	# 	return result

def main():
	print(Solution().intersect([5, 8, 8, 14, 1, 2, 3, 1], [4, 2, 8, 5, 1, 1]))

if __name__ == "__main__":
	main()

