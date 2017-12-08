"""
how we convert an int to binary?
let's say the int is 28

28 % 2 = 0
28 / 2 = 14

14 % 2 = 0
14 / 2 = 7

7 % 2 = 1
7 / 2 = 3

3 % 2 = 1
3 / 2 = 1

1 % 2 = 1
1 / 2 = 0

the result is
11100

here is the same, but this time, every 26 count, will do a carry
"""

class Solution():
	def convertTotitle(self, n):
		result = ""
		while n:
			"""
			I am doing this to handle when number is 26 or 52, etc
			one edge case is 26
			if it is n % 26, which means it is an 'Z'
			also, when n = n // 26, it will cause an error that do one more iteration
			"""
			(n, offset) = (n, n % 26 -1) if n % 26 != 0 else (n - 1, 25)
			result = chr(ord('A') + offset) + result
			n = n // 26
		return result

def main():
	print(Solution().convertTotitle(26))

if __name__ == "__main__":
	main()