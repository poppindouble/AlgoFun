class Solution:
	def reverseWords(self, s):
		return " ".join(map(lambda x: x[::-1], list(s.split())))


def main():
	print(Solution().reverseWords("Let's take LeetCode contest"))

if __name__ == "__main__":
	main()