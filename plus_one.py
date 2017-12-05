"""
Idea is pretty simple.
Consider two situation:
last digit is < 9
last digit is == 9
if it is the second situation, traverse from behind, find the first digit which is < 9
else after the loop it become 10000....000
"""

class Solution:
	def plusOne(self, digits):
		if digits[-1] < 9:
			return digits[:-1] + [digits[-1] + 1]
		else:
			for i in range(len(digits) - 1, -1, -1):
				if digits[i] < 9:
					digits[i] = digits[i] + 1
					return digits
				else:
					digits[i] = 0
			return [1] + [0] * len(digits)


def main():
	print(Solution().plusOne([5, 6, 7, 8, 9]))

if __name__ == "__main__":
	main()