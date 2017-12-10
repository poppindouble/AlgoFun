"""
we can solve it in a really straight forward way
convert binary to string, and pad it with zero and conver it back to integer
this method doesn't use any bit manupulation of bits

another way to do it is by using bit manupulation
To check a integer in binary is "{0:b}.format(37)"

<< is left shit binary number,
"{0:b}".format(0 << 1) => "0"
"{0:b}".format(0 << 20) => "0"
"{0:b}".format(1 << 1) => "10"
"{0:b}".format(1 << 2) => "100"

| is bit or operator
"{0:b}".format(1 | 1) = "1"
"{0:b}".format(1 | 0) = "1"
"{0:b}".format(0 | 0) = "0"

& is bit and operator
"{0:b}".format(1 & 1) = "1"
"{0:b}".format(1 & 0) = "0"
"{0:b}".format(0 & 0) = "0"
"""

class Solution:
	# def reverseBits(self, n):
	# 	return self.stringToInt(self.intToString(n))

	# def intToString(self, n):
	# 	result = ""
	# 	while n:
	# 		temp = n % 2
	# 		result = str(temp) + result
	# 		n = n // 2
	# 	for i in range(32 - len(result)):
	# 		result = '0' + result
	# 	return result

	# def stringToInt(self, s):
	# 	result = 0
	# 	for i, c in enumerate(s[::-1]):
	# 		if c == '1':
	# 			result = result + pow(2, i)
	# 	return result

	def reverseBits(self, n):
		result = 0
		for i in range(32):
			result <<= 1
			result |= n & 1
			n >>= 1
		return result

def main():
	print(Solution().reverseBits(43261596))

if __name__ == "__main__":
	main()