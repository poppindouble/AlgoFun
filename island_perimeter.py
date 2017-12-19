class Solution:
	def islandPerimeter(self, grid):
		width = len(grid[0])
		height = len(grid)
		result = 0
		for x in range(height):
			for y in range(width):
				if grid[x][y] == 1:
					arround = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
					for (i, j) in arround:
						if i < 0 or i >= height:
							result += 1
						elif j < 0 or j >= width:
							result += 1
						elif grid[i][j] == 0:
							result += 1
		return result


def main():
	# island = [
	# [0, 1, 0, 0],
	# [1, 1, 1, 0],
	# [0, 1, 0, 0],
	# [1, 1, 0, 0]
	# ]
	island = [
	[1, 0]
	]
	print(Solution().islandPerimeter(island))

if __name__ == "__main__":
	main()