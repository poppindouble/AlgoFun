class Solution:
	def isPowerOfThree(self, n):
		while n % 3 == 0:
			n //= 3
		return n == 1

def main():
	print(Solution().isPowerOfThree(81))
	print(Solution().isPowerOfThree(91))
	print(Solution().isPowerOfThree(27))

if __name__ == "__main__":
	main()