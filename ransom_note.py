from collections import Counter

class Solution():
	def canConstruct(self, ransomNote, magazine):
		myDict = Counter(magazine)
		for char in ransomNote:
			if char not in myDict:
				return False
			if myDict[char] == 0:
				return False
			myDict[char] -= 1
		return True


def main():
	print(Solution().canConstruct("aaa", "aab"))

if __name__ == "__main__":
	main()