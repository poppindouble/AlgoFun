from collections import Counter
class Solution:
	def firstUniqChar(self, s):
		myDict = Counter(s)
		for index, char in enumerate(s):
			if myDict[char] == 1:
				return index
		return -1

def main():
	print(Solution().firstUniqChar("loveleetcode"))

if __name__ == "__main__":
	main()