class Solution:
	def toHex(self, num):
		if num == 0:
			return 0
		negative = num < 0
		result = ""
		while num:
			lastDigit = num % 16
			if lastDigit >= 10:
				lastDigit = chr(lastDigit - 10 + ord('a'))

			result = str(lastDigit) + result
			num //= 16
		return result

def main():
	print(Solution().toHex(-26))

if __name__ == "__main__":
	main()