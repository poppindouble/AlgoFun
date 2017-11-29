class Solution:
	def reverse(self, x):
		result = 0
		isNegative = False
		if x < 0:
			isNegative, x = True, -x
		while x > 0:
			lastDigit = x % 10
			result = result * 10 + lastDigit
			x = x // 10
		if isNegative:
			result = -result
		# python will convert 
		if result < -(1 << 31) or result > (1 << 31) - 1:
			return 0
		return result

def main():
	print(Solution().reverse(-123))

if __name__ == "__main__":
	main()