"""
In python, str.split()
if we specifiy the seperator
for example, "1,2,3,,,4".split(',')
we will get ['1', '2', '3', '', '', '4']

if we don't specific the seperator
for example "    1  2 3   4".split(' ')
you will get ['1', '2', '3', '4']

https://docs.python.org/3/library/stdtypes.html#str.split
"""

class Solution:
	def lengthOfLastWord(self, s):
		if not len(s.split()):
			return 0
		return len(s.split()[-1])


def main():
	print(Solution().lengthOfLastWord("hello world"))

if __name__ == "__main__":
	main()