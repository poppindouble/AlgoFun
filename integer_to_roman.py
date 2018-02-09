class Solution:
	def intToRoman(self, num):
		base = 1
		result = ""
		while num:
			digit = num % 10
			result = self.__numToRoman__(digit, base) + result
			base *= 10
			num //= 10
		return result

	def __numToRoman__(self, num, base):
		paras = ('I', 'V', 'X')
		if base == 10:
			paras = ('X', 'L', 'C')
		if base == 100:
			paras = ('C', 'D', 'M')
		if base == 1000:
			return 'M' * num
		if num <= 3:
			return paras[0] * num
		if num == 4:
			return paras[0] + paras[1]
		if 5 <= num <= 8:
			return paras[1] + (num - 5) * paras[0]
		if num == 9:
			return paras[0] + paras[2]


def main():
	print(Solution().intToRoman(2390))

if __name__ == "__main__":
	main()