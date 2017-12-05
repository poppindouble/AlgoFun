class Solution:
	def addBinary(self, a, b):
		num1 = a[::-1]
		num2 = b[::-1]
		result = ''
		carry = 0
		for i in range(max(len(num1), len(num2))):
			x = int(num1[i]) if i < len(num1) else 0
			y = int(num2[i]) if i < len(num2) else 0
			result = "{}".format((x + y + carry) % 2) + result
			carry = (x + y + carry) // 2
		if carry:
			result = '1' + result

		return result


def main():
	print(Solution().addBinary("11111", "11"))

if __name__ == "__main__":
	main()