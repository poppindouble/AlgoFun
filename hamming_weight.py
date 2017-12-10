class Solution():
	def hammingWeight(self, n):
		result = 0
		for _ in range(32):
			if n & 1:
				result += 1
			n >>= 1
		return result

def main():
	print(Solution().hammingWeight(11))

if __name__ == "__main__":
	main()