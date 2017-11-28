# Determine whether an integer is a palindrome. Do this without extra space.

# this solution is to reverse the integer, however it used extra space
class Solution:
	def isPalindrome(self, x):
		if x < 0:
			return False
		result = 0
		y = x
		while y != 0:
			lastDigit = y % 10
			result = result * 10 + lastDigit
			y = y // 10
		return result == x

	def isPalindromeNoExtraSpace(self, x):
		if x < 0:
			return False
		digit = 1
		while x // digit >= 10:
			digit = digit * 10

		while x:
			if self.__firstDigitIsEqualToLastOne__(x, digit):
				x = x % digit // 10
				digit = digit // 100
				print(x)
			else:
				return False
		return True


	def __firstDigitIsEqualToLastOne__(self, num, digit):
		firstDigit = num // digit
		lastDigit = num % 10
		return firstDigit == lastDigit

def main():
	print(Solution().isPalindrome(-2147483648))
	print(Solution().isPalindromeNoExtraSpace(1000021))

if __name__ == "__main__":
	main()