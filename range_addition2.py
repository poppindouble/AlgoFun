import sys

class Solution:
	def maxCount(self, m, n, ops):
		row, col = m, n
		for op in ops:
			row = min(row, op[0])
			col = min(col, op[1])
		return row * col

def main():
	print(Solution().maxCount(3, 3, [[2, 2], [3, 3]]))

if __name__ == "__main__":
	main()