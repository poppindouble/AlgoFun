class Solution:
	def detectCapitalUse(self, word):
		rule1 = all(map(lambda x: x.isupper(), word))
		rule2 = all(map(lambda x: not x.isupper(), word))
		rule3 = True
		if len(word) >= 2:
			rule3 = word[0].isupper() and all(map(lambda x: not x.isupper(), word[1:]))
			return rule3 or rule2 or rule1
		return rule1 or rule2

def main():
	print(Solution().detectCapitalUse("Leetcode"))

if __name__ == "__main__":
	main()