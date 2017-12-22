class Solution:
	def convertToBase7(self, num):
		if num == 0:
			return 0
		isNeg = num < 0
		result = ""
		while num:
			result = str(num % 7) + result
			num //= 7
		if isNeg:
			return "-" + result
		return result

def main():
	print(Solution().convertToBase7(2932))

if __name__ == "__main__":
	main()