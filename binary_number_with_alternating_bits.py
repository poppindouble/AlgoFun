class Solution:
	def hasAlternatingBits(self, n):
		expected = n & 1
		while n:
			lastBit = n & 1
			if lastBit != expected:
				return False
			expected = 0 if expected == 1 else 1
			n = n >> 1
		return True

def main():
	print(Solution().hasAlternatingBits(5))

if __name__ == "__main__":
	main()