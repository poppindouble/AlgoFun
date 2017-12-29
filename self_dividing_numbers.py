class Solution:
	def selfDividingNumbers(self, left, right):
		return list(filter(self.isDividingNumber, range(left, right+1)))

	def isDividingNumber(self, num):
		temp = num
		while temp:
			lastDigit = temp % 10
			if lastDigit == 0 or num % lastDigit != 0:
				return False
			temp //= 10
		return True

def main():
	print(Solution().selfDividingNumbers(1, 22))

if __name__ == "__main__":
	main()