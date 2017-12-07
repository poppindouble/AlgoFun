class Solution:
	def generate(self, numRows):
		result = []
		if numRows == 1:
			result.append([1])
		if numRows >= 2:
			result.append([1])
			result.append([1, 1])
		for i in range(2, numRows):
			previous = result[-1]
			temp = [0] * (i + 1)
			for k in range(i + 1):
				if k == 0 or k == i:
					temp[k] = 1
				else:
					temp[k] = previous[k] + previous[k - 1]
			result.append(temp)
		return result



def main():
	print(Solution().generate(5))

if __name__ == "__main__":
	main()