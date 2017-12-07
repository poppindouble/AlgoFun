class Solution:
	def generate(self, rowIndex):
		result = [1] * (rowIndex + 1)
		for i in range(2, rowIndex + 1):
			for k in range(i - 1, 0, -1):
				result[k] = result[k] + result[k - 1]
		return result

def main():
	print(Solution().generate(5))

if __name__ == "__main__":
	main()