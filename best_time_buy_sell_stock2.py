class Solution:
	def maxProfit(self, prices):
		if len(prices) <= 1:
			return 0
		minimum = prices[0]
		profit = 0
		for currentPrice in prices[1:]:
			if currentPrice < minimum:
				minimum = currentPrice
			else:
				profit = profit + currentPrice - minimum
				minimum = currentPrice
		return profit

def main():
	print(Solution().maxProfit([3, 6, 5, 1, 7, 4]))

if __name__ == "__main__":
	main()