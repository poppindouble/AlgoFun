class Solution:
	def countBinarySubstrings(self, s):
		if len(s) <= 1:
			return 0
		counter = 0
		j = 1
		while j < len(s):
			if s[j - 1] != s[j]:
				i = j - 1
				counter += 1
				while i > 0 and j < len(s) - 1 and s[i] == s[i - 1] and s[j] == s[j + 1]:
					j += 1
					i -= 1
					counter += 1
			j += 1
		return counter



def main():
	print(Solution().countBinarySubstrings("00110011"))

if __name__ == "__main__":
	main()