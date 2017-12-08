class Solution:
	def titleToNumber(self, s):
		result = 0
		for index, c in enumerate(s[::-1]):
			result = result + (ord(c) - 64) * pow(26, index)
		return result

def main():
	print(Solution().titleToNumber("AA"))

if __name__ == "__main__":
	main()