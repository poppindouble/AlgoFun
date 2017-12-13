class Solution:
	# def wordPattern(self, pattern, str):
	# 	if len(pattern) != len(str.split()): return False
	# 	ptnDict, wordDict = {}, {}
	# 	for ptn, word in zip(pattern, str.split()):
	# 		if ptn not in ptnDict:
	# 			ptnDict[ptn] = word
	# 		if word not in wordDict:
	# 			wordDict[word] = ptn
	# 		if wordDict[word] != ptn or ptnDict[ptn] != word:
	# 			return False
	# 	return True

	def wordPattern(self, pattern, str):
		t = str.split()
		print(list(map(pattern.find, pattern)))
		print(list(map(t.index, t)))
		return list(map(pattern.find, pattern)) == list(map(t.index, t))

def main():
	print(Solution().wordPattern("abba", "dog cat cat dog"))

if __name__ == "__main__":
	main()