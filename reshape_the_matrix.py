"""
avoid use [[0] * c] * r to construct 2d array
it gonna be shallow copy
a = [ [0] * 3 ] * 3
print(a) => [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a[0][0] = 1
print(a) => [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
all the rest of the list will be the same ref as the first one
http://www.kosbie.net/cmu/fall-11/15-112/handouts/notes-2d-lists.html
"""


class Solution:
	def matrixReshape(self, nums, r, c):
		row = len(nums)
		col = len(nums[0])

		if r * c != row * col:
			return nums

		result = [[0 for col in range(c)] for row in range(r)]
		i = j = 0
		for rowIndex in range(row):
			for colIndex in range(col):
				result[i][j] = nums[rowIndex][colIndex]
				j += 1
				if j == c:
					i += 1
					j = 0
		return result

def main():
	print(Solution().matrixReshape([[1, 2], [3, 4]], 4, 1))

if __name__ == "__main__":
	main()