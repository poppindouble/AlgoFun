"""
s = {1:2, 3:4}
s[1] -> 1
s[0] -> error
"""

class Solution:
	def intersection(self, nums1, nums2):
		dict = {}
		result = []
		for num in nums1:
			dict[num] = 1
		for num in nums2:
			if num in dict and dict[num] == 1:
				result.append(num)
				dict[num] = -1
		return result

def main():
	print(Solution().intersection([], [1]))

if __name__ == "__main__":
	main()