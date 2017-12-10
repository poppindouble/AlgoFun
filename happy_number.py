"""
let's say 19:
1^2 + 9 ^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

let's say 11:
1^2 + 1^2 = 2
2^2 = 4
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4

4 appear again, use set to solve this problem
"""

class Solution:
	def isHappy(self, n):
		result = n
		seen = set()

		while result != 1 and result not in seen:
			seen.add(result)
			result = self.__digitSum__(result)

		if result == 1:
			return True
		else:
			return False

	def __digitSum__(self, n):
		result = 0
		while n:
			result = result + pow((n % 10), 2)
			n = n // 10
		return result

def main():
	print(Solution().isHappy(11))

if __name__ == "__main__":
	main()