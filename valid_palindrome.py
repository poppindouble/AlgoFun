class Solution:
	def isPalindrome(self, s):
		head = 0
		tail = len(s) - 1

		while head <= tail:
			if not (s[head].isalpha() or s[head].isdigit()):
				head += 1
				continue
			if not (s[tail].isalpha() or s[tail].isdigit()):
				tail -= 1
				continue
			if s[head].lower() == s[tail].lower():
				head += 1
				tail -= 1
			else:
				return False
		return True

def main():
	print(Solution().isPalindrome("0p"))

if __name__ == "__main__":
	main()