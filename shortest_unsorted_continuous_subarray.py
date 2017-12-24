import sys

class Solution:
	# def findUnsortedSubarray(self, nums):
	# 	stack = []
	# 	for num in nums:
	# 		while stack and stack[-1] > num:
	# 			stack.pop()
	# 		stack.append(num)

	# 	left = None
	# 	for index, num in enumerate(stack):
	# 		if num != nums[index]:
	# 			break
	# 		left = index

	# 	stack.clear()
	# 	for num in nums[::-1]:
	# 		while stack and stack[-1] < num:
	# 			stack.pop()
	# 		stack.append(num)

	# 	right = None
	# 	for index, num in enumerate(stack):
	# 		if num != nums[len(nums) - 1 - index]:
	# 			break
	# 		right = len(nums) - 1 - index
		
	# 	if left != None and right != None:
	# 		return(left + 1, right - 1)
	# 	if left == None and right != None:
	# 		return(0, right - 1)
	# 	if right == None and left != None:
	# 		return(left + 1, len(nums) - 1)
	# 	if left == None and right == None:
	# 		return(0, len(nums) - 1)

"""
This solution is so close, but could't handle duplicated nums properly
	def findUnsortedSubarray(self, nums):
        temp = [len(nums), sys.maxsize]
        i, j = 0, 1
        right = len(nums) - 1
        while j < len(nums):
            if nums[j] <= nums[i]:
                right = j
                if nums[j] < temp[1]:
                    temp[0] = i
                    temp[1] = nums[j]
                    while nums[temp[0]] > nums[j]:
                        temp[0] -= 1
                        if temp[0] == -1:
                            break
                    temp[0] += 1
            i += 1
            j += 1
        return right - temp[0] + 1
"""
	def findUnsortedSubarray(self, nums):
		left = right = -1
		maxNum = nums[0]
		minNum = nums[-1]
		for i in range(1, len(nums)):
			maxNum = max(maxNum, nums[i])
			minNum = min(minNum, nums[len(nums)-1-i])
			if nums[i] < maxNum:
				right = i
			if nums[len(nums)-1-i] > minNum:
				left = len(nums)-1-i
		if left == right == -1:
			return 0
		return right - left + 1
def main():
	print(Solution().findUnsortedSubarray([1,3,2,2,2,2,2,4,5,6,7]))
	# 1,2,3,3,3,3,3,4,5,6,7
	# 1,3,2,2,2,2,2,4,5,6,7

if __name__ == "__main__":
	main()