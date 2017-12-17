"""
dictionary is the sliding window
it represent, for each element in p,
if the value of the char in p is positive,
means we need this much number of this char to make anagram

0 means just enough of char to say it is anagram
negative means too much

pLen represent how many char in p is already qualified to be anagram
when we remove element from the window
if this element is in the p
and also
the value in the dictionary of this element is >= 0
which means, the current window, including thie element itself
make enough to be an anagram, so the pLen += 1
else
if the value in the dictionary of this element is < 0
mean, the current window, incuding this element itself
have too much of this element.
so just don't touch pLen
"""

from collections import Counter

class Solution:
	def findAnagrams(self, s, p):
		result = []
		current = 0
		pDict = Counter(p)
		pLen = len(p)
		last = 0

		for index, char in enumerate(s):
			print(pDict, char)
			if char in pDict:
				if pDict[char] >= 1:
					pLen -= 1
				pDict[char] -= 1
				if pLen == 0:
					result.append(index - len(p) + 1)

			if index >= len(p) - 1:
				if s[last] in pDict:
					if pDict[s[last]] >= 0:
						pLen += 1
					pDict[s[last]] += 1
				last += 1

			print(pDict, char)

		return result

def main():
	print(Solution().findAnagrams("cbaebabacd", "abc"))

if __name__ == "__main__":
	main()