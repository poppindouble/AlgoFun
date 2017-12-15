class Solution:
	def fizzBuzz(self, n):
		result = []
		for i in range(1, n + 1):
			temp = ""
			if i % 3 == 0:
				temp += "Fizz"
			if i % 5 == 0:
				temp += "Buzz"
			if not temp:
				temp = str(i)
			result.append(temp)
		return result

def main():
	print(Solution().fizzBuzz(15))

if __name__ == "__main__":
	main()