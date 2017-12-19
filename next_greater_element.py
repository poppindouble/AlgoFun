class Solution:
	def nextGreaterElement(self, nums1, nums2):
		stack = []
		dict = {}
		result = []
		for num in nums2:
			while stack and stack[-1] < num:
				dict[stack.pop()] = num
			stack.append(num)

		return [dict.get(num, -1) for num in nums1]

def main():
	print(Solution().nextGreaterElement([4,1,2], [8,5,4,2,1,3,7,6,9]))

if __name__ == "__main__":
	main()