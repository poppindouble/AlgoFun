class Solution:
	def checkPerfectNumber(self, num):
		root = int(num ** 0.5)
		result = 1
		for i in range(2, root + 1):
			if num % i == 0:
				result = result + i + num // i
		return result == num

def main():
	print(Solution().checkPerfectNumber(2))

if __name__ == "__main__":
	main()