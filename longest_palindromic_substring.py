"""
the first solution will be time out of limited
because it actually check all the substring and then each of the substring
we are checking if it is palindrome. so complexity is n*(2^n)

second solution is from leetcode, but python can not pass the time limit,
complexity is n^2
we need to construct a 2D array, result.
result[i][j] represent if s[i:j] is a palindrome
result[i][j]

third solution is the best, everytime if we add a char to the string
when you increase s by 1 character, if new maxPalindrome includes this new character.
you could only increase maxPalindromeLen by 1 or 2

for example
abc
when we add another c into abc
abcc
the maxPalindrome now is cc(it inculde the new c)
the maxPalindromeLen is 2 now, before it was 1

b
when we add another b in to "b"
bb
the maxPalindrome now is bb(it inculde the new b)
the maxPalindromeLen is 2 now, before it was 1

aa
when we add another a into "aa"
aaa
the maxPalindrome now is aaa(it inculde the new a)
the maxPalindromeLen is 3 now, before it was 2

baa
when we add another b into "baa"
baab
the maxPalindrome now is baab(it inculde the new b)
the maxPalindromeLen is 4 now, before it was 2

proof
let's say when we add a new character, if new maxPalindrome ends at this new character
and let's say the new maxPalindrome length is Q, then we should have:
Q - 2 <= P
Q <= P + 2
so the initial case is that the P is 1
we start from second element,
for every element s[i] we check if s[i - P : i + 1]
or s[i - P - 1 : i + 1] is palindrome
if it is, we update start poistion and P 

one good example:
acbababcddcba
initial:
c, P = 1
b, P = 1
a, P = 1
b, P = 3 (bab)
a, P = 3
b, P = 5 (babab)
c, P = 7 (cbababc)
d, P = 7
d, P = 7
c, P = 7
b, P = 7
a, P = 8 (abcddcba)

the last solution is expand from middle
"""

class Solution:
	# def longestPalindrome(self, s):
	# 	if self.__isPalindrome__(s):
	# 		return s
	# 	if self.__isPalindrome__(s[1:]):
	# 		return s[1:]
	# 	if self.__isPalindrome__(s[:-1]):
	# 		return s[:-1]

	# 	left = self.longestPalindrome(s[1:])
	# 	right = self.longestPalindrome(s[:-1])
	# 	result = left if len(left) > len(right) else right
	# 	return result

	# def __isPalindrome__(self, s):
	# 	return s == s[::-1]

	# def longestPalindrome(self, s):
	# 	ans = s[0]
	# 	result = [[True if row == col else False for col in range(len(s))] for row in range(len(s))]
	# 	for row in range(len(s)-2, -1, -1):
	# 		for col in range(row+1, len(s)):
	# 			if col == row + 1:
	# 				if s[row] == s[col]:
	# 					result[row][col] = True
	# 					ans = s[row:col+1] if len(s[row:col+1]) > len(ans) else ans
	# 				continue
	# 			if s[row] == s[col] and result[row+1][col-1]:
	# 				result[row][col] = True
	# 				ans = s[row:col+1] if len(s[row:col+1]) > len(ans) else ans
	# 			else:
	# 				result[row][col] = False
	# 	return ans

	# def longestPalindrome(self, s):
	# 	maxPalindromeLen = 1
	# 	start = 0
	# 	for index in range(1, len(s)):
	# 		if index - maxPalindromeLen >= 1 and s[index-maxPalindromeLen-1:index+1] == s[index-maxPalindromeLen-1:index+1][::-1]:
	# 			start = index - maxPalindromeLen - 1
	# 			maxPalindromeLen += 2
	# 		elif index - maxPalindromeLen >= 0 and s[index-maxPalindromeLen:index+1] == s[index-maxPalindromeLen:index+1][::-1]:
	# 			start = index - maxPalindromeLen
	# 			maxPalindromeLen += 1
	# 	return s[start:start+maxPalindromeLen]

	# def longestPalindrome(self, s):
	# 	start = end = 0
	# 	for index, c in enumerate(s):
	# 		len1 = self.__findLengthOfPalindrom__(s, index, index)
	# 		len2 = self.__findLengthOfPalindrom__(s, index, index+1)
	# 		if len1 > (end - start + 1) or len2 > (end - start + 1):
	# 			start = index - (len1 - 1) // 2 if len1 > len2 else index - len2 // 2 + 1
	# 			end = index + (len1 - 1) // 2 if len1 > len2 else index + len2 // 2
	# 	return s[start:end+1]

	# def __findLengthOfPalindrom__(self, s, centerLeft, centerRight):
	# 	left = centerLeft
	# 	right = centerRight
	# 	while left >= 0 and right < len(s) and s[left] == s[right]:
	# 		left -= 1
	# 		right += 1
	# 	return right - left - 1

	def longestPalindrome(self, s):
		result = ""
		for index, c in enumerate(s):
			offset = 0
			if index < len(s) - 1 and s[index] == s[index+1]:
				while (index-offset >= 0 and index+1+offset < len(s) and s[index+1+offset] == s[index-offset]):
					if len(s[index-offset : index+offset+1+1]) > len(result):
						result = s[index-offset : index+offset+1+1]
					offset += 1
			else:
				while (index+offset < len(s) and index-offset >= 0 and s[index+offset] == s[index-offset]):
					if len(s[index-offset : index+offset+1]) > len(result):
						result = s[index-offset : index+offset+1]
					offset += 1
		return result

def main():
	# print(Solution().longestPalindrome("lejyqjcpluiggwlmnumqpxljlcwdsirzwlygexejhvojztcztectzrepsvwssiixfmpbzshpilmojehqyqpzdylxptsbvkgatzdlzphohntysrbrcdgeaiypmaaqilthipjbckkfbxtkreohabrjpmelxidlwdajmkndsdbbaypcemrwlhwbwaljacijjmsaqembgtdcskejplifnuztlmvasbqcyzmvczpkimpbbwxdtviptzaenkbddaauyvqppagvqfpednnckooxzcpuudckakutqyknuqrxjgfdtsxsoztjkqvfvelrklforpjnrbvyyvxigjhkjmxcphjzzilvbjbvwiwnnkbmboiqamgoimujtswdqesighoxsprhnsceshotakvmoxqkqjvbpqucvafiuqwmrlfjpjijbctfupywkbawquchbclgvhxbanybret"))
	print(Solution().longestPalindrome("cbbd"))
if __name__ == "__main__":
	main()