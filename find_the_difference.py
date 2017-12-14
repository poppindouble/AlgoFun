from collections import Counter

class Solution:
	def findTheDifference(self, s, t):
		myDict = Counter(s)
		for char in t:
			if char not in myDict:
				return char
			if myDict[char] == 0:
				return char
			myDict[char] -= 1

def main():
	print(Solution().findTheDifference("abcdacdklg", "cdabladkgce"))

if __name__ == "__main__":
	main()