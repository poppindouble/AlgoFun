"""
This solution we used normal thinking
time complexity is O(logn)

there is another solution, which is O(1) time
and O(1) space

1	1
2	10
4	100
8	1000
16	10000

if a number is power of 2, it only has one 1 in its binary
if the number - 1, then except the most left bit, the rest will be 0
if we do &, we should get 0
"""

class Solution:
	# def isPowerOfTwo(self, n):
	# 	if n == 0:
	# 		return False
	# 	while n != 1:
	# 		if n % 2 != 0:
	# 			return False
	# 		n //= 2
	# 	return True

	# def isPowerOfTwo(self, n):
	# 	counter = 0
	# 	while n:
	# 		counter += 1 & n
	# 		n <<= 1
	# 	return counter == 1


	def isPowerOfTwo(self, n):
		return (n > 0) and not (n & (n - 1))

def main():
	print(Solution().isPowerOfTwo(1024))

if __name__ == "__main__":
	main()