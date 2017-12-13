class Solution:
	def isPowerOfFour(self, n):
		return n > 0 and not (n & (n - 1)) and (n & 0x55555555) == n

def main():
	print(Solution().isPowerOfFour(16))
	print(Solution().isPowerOfFour(32))
	print(Solution().isPowerOfFour(22))

if __name__ == "__main__":
	main()