class Solution:
	def convert(self, s, numRows):
		if len(s) <= numRows or numRows == 1:
			return s
		matrix = ['' for i in range(numRows)]
		step = 1
		index = 0
		for c in s:
			matrix[index] += c
			if index == 0:
				step = 1
			elif index == numRows - 1:
				step = -1
			index += step
		return ''.join(matrix)

def main():
	print(Solution().convert("ABCDEFGHIJKLMNOPQ", 6))

if __name__ == "__main__":
	main()