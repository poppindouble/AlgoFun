"""
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8    
9    9    
10    1
11    2
12    3    
13    4
14    5
15    6
16    7
17    8
18    9
19    1
20    2

when num > 9
the result is just num % 9
"""

class Solution:
	# def addDigits(self, num):
	# 	result = num
	# 	while result >= 10:
	# 		num = result
	# 		result = 0
	# 		while num:
	# 			result = result + num % 10
	# 			num = num // 10
	# 	return result

	def addDigits(self, num):
		return (num - 1) % 9 + 1

def main():
	print(Solution().addDigits(6324))

if __name__ == "__main__":
	main()