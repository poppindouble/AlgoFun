"""
python3 has sys.maxsize

This number may appear to be arbitrary, but it isn't. 
9223372036854775807 is exactly 2^63 - 1, 
so you've got a 64-bit int. In general, 
an n-bit integer has values ranging from -2^(n-1) to 2^(n-1) - 1

Note that if you're using a 32-bit Python runtime, 
sys.maxsize will return 2^31 - 1, 
even though Python will jump to 64-bit seamlessly with the long datatype

if python is running on a 64 bits platform
which is 2 ^ 63 - 1, that's the max int on a 64 bits platform
so, the minimum gonna be -(sys.maxsize + 1), but this will overflow
so minimum should be -sys.maxsize - 1

so python3, int range:
[-sys.maxsize - 1, sys.maxsize(whihc is 2 ^63 - 1)]

"""
import sys
class Solution:
	# def thirdMax(self, nums):
		# newNums = list(set(nums))
		# if len(newNums) < 3:
		# 	return max(newNums)
		# [third, second, first] = sorted(newNums[0:3])
		# for i in newNums[3:]:
		# 	if i > first:
		# 		first, second, third = i, first, second
		# 	elif i > second:
		# 		third = second
		# 		second = i
		# 	elif i > third:
		# 		third = i
		# return third

	def thirdMax(self, nums):
		first = second = third = -sys.maxsize - 1
		for n in nums:
			if n > first:
				first, second, third = n, first, second
			elif n > second and n < first:
				second, third = n, second
			elif n > third and n < second:
				third = n
		if third == -sys.maxsize - 1:
			return max(first, second)
		return third

def main():
	print(Solution().thirdMax([1,2,2,5,3,5]))

if __name__ == "__main__":
	main()