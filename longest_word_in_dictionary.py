"""
the description about this question is pretty stupid
one character at a time by other words in words is really really confusing
the straightforward explaination is find the longest word
whose all the prefix is in dictionary
"""
class Solution:
	def longestWord(self, words):
		mySet = set([""])
		result = ""
		for word in sorted(words):
			if word[:-1] in mySet:
				mySet.add(word)
				result = word if len(word) > len(result) else result
		return result

def main():
	print(Solution().longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]))

if __name__ == "__main__":
	main()