class Solution:
	def findComplement(self, num):
		mask = 1
		num2 = num
		while num2:
			mask = (mask << 1) + 1
			num2 = num2 >> 1
		return (mask >> 1) ^ num

def main():
	print(Solution().findComplement(5))

if __name__ == "__main__":
	main()