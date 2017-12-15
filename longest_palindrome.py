from collections import Counter

class Solution:
	def longestPalindrome(self, s):
		myDict = Counter(s)
		plusOne = 0
		result = 0
		for _, val in myDict.items():
			if val % 2 != 0:
				plusOne = 1
				val -= 1
			result += val
		return result + plusOne

def main():
	print(Solution().longestPalindrome("abccccdd"))

if __name__ == "__main__":
	main()