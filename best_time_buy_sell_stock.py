class Solution:
	def maxProfit(self, prices):
		if not prices:
			return 0
		minimum = prices[0]
		profit = 0
		for currentPrice in prices[1:]:
			if currentPrice < minimum:
				minimum = currentPrice
			else:
				profit = max(profit, currentPrice - minimum)
		return profit

def main():
	print(Solution().maxProfit([6, 3, 5]))

if __name__ == "__main__":
	main()