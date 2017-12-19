class Solution:
	def hammingDistance(self, x, y):
		temp = x ^ y
		result = 0
		while temp:
			result += temp & 1
			temp = temp >> 1
		return result

def main():
	print(Solution().hammingDistance(1, 4))

if __name__ == "__main__":
	main()