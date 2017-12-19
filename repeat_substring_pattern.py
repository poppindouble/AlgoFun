class Solution:
	def repeatedSubstringPattern(self, s):
		if len(s) < 2:
			return False
		next = [0] * len(s)
		i, j = 0, 1
		while j < len(s):
			if s[j] == s[i]:
				next[j] = i + 1
				i += 1
				j += 1
			else:
				if i == 0:
					next[j] = 0
					j += 1
				else:
					i = next[i - 1]
		return next[-1] > 0 and len(s) % (len(s) - next[-1]) == 0

def main():
	print(Solution().repeatedSubstringPattern("abaababaab"))

if __name__ == "__main__":
	main()