class Solution:
	def reverseVowels(self, s):
		vowels = ['a', 'e', 'i', 'o', 'u']
		str = list(s)
		head = 0
		tail = len(s) - 1
		while head < tail:
			if str[head] not in vowels:
				head += 1
				continue
			if str[tail] not in vowels:
				tail -= 1
				continue
			str[head], str[tail] = str[tail], str[head]
			head += 1
			tail -= 1


		return "".join(str)


def main():
	print(Solution().reverseVowels("hello"))
	print(Solution().reverseVowels("leetcode"))
	print(Solution().reverseVowels("leetecode"))
	print(Solution().reverseVowels("aaaaaa"))
	print(Solution().reverseVowels("bbbbbb"))

if __name__ == "__main__":
	main()