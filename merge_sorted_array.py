"""
let's say 
nums1 = [6, 7, 8]
nums2 = [1, 2, 3, 4, 5]

if we start from begining of nums1 to construct the final result
then we need to move 3 elements everytime.
so the complexity will be pretty high, which is gonna be O(m * n)

if we start from behind
then the complexity will be O(m + n)

"""


class Solution:
	def merge(self, nums1, m, nums2, n):
		i = m - 1
		j = n - 1
		for index in range(m + n - 1, -1, -1):
			if j < 0:
				break
			if i < 0:
				nums1[0:index+1] = nums2[0:j+1]
				break

			if nums1[i] <= nums2[j]:
				nums1[index] = nums2[j]
				j -= 1
			else:
				nums1[index] = nums1[i]
				i -= 1
		return nums1

	# def merge(self, nums1, m, nums2, n):
	# 	while m > 0 and n > 0:
	# 		if nums1[m - 1] <= nums2[n - 1]:
	# 			nums1[m + n - 1] = nums2[n - 1]
	# 			n -= 1
	# 		else:
	# 			nums1[m + n - 1] = nums1[m - 1]
	# 			m -= 1
	# 	if n > 0:
	# 		nums1[:n] = nums2[:n]
	# 	return nums1

def main():
	print(Solution().merge([1, 2, 4, 5, 6, 0], 5, [3], 1))
	"""
	final result [1, 2, 3, 4, 5, 6, 7, 9, 10, 10, 29]
	"""

if __name__ == "__main__":
	main()