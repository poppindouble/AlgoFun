class Solution:
	def arrangeCoins(self, n):
		row = 1
		while n >= row:
			n -= row
			row += 1
		return row - 1

def main():
	print(Solution().arrangeCoins(5))

if __name__ == "__main__":
	main()