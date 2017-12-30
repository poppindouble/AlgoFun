class Solution:
	# def lengthOfLongestSubstring(self, s):
	# 	result = -1
	# 	i, j = 0, 0
	# 	mySet = set()
	# 	while j < len(s):
	# 		if s[j] not in mySet:
	# 			mySet.add(s[j])
	# 			j += 1
	# 		else:
	# 			result = max(result, j - i)
	# 			while s[i] != s[j]:
	# 				mySet.remove(s[i])
	# 				i += 1
	# 			mySet.remove(s[i])
	# 			i += 1
	# 	return max(result, j-i)

	def lengthOfLongestSubstring(self, s):
		ans, start, end = 0, 0, 0
		countDict = {}
		for c in s:
			end += 1
			countDict[c] = countDict.get(c, 0) + 1
			while countDict[c] > 1:
				countDict[s[start]] -= 1
				start += 1
			ans = max(ans, end - start)
		return ans

def main():
	print(Solution().lengthOfLongestSubstring("bbbbb"))

if __name__ == "__main__":
	main()