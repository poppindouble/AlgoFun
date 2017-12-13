class Solution:
	def reverseString(self, s):
		return s[::-1]

def main():
	print(Solution().reverseString("hello"))

if __name__ == "__main__":
	main()