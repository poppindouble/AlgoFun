class Solution:
	def isUgly(self, num):
		while num % 2 == 0:
			num //= 2
		while num % 3 == 0:
			num //= 3
		while num % 5 == 0:
			num //= 5
		return num == 1

def main():
	print(Solution().isUgly(14))

if __name__ == "__main__":
	main()