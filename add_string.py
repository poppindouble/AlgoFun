class Solution:
	def addStrings(self, num1, num2):
		result = ""
		num1 = num1[::-1]
		num2 = num2[::-1]
		n = len(num1)
		m = len(num2)
		carry = 0
		for i in range(max(m, n)):
			if i < n and i < m:
				temp = int(num1[i]) + int(num2[i]) + carry
			else:
				larger = num1 if n > m else num2
				temp = int(larger[i]) + carry
			carry = temp // 10
			result += str(temp % 10)
			result = result[::-1]
		if carry:
			return '1' + result
		return result

def main():
	print(Solution().addStrings("1", "9999"))

if __name__ == "__main__":
	main()