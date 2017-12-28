class Solution:
	def maxAreaOfIsland(self, grid):
		self.grid = grid
		result = 0
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if self.grid[row][col] == 1:
					# result = max(result, self.dfs(row, col))
					result = max(result, self.bfs(row, col))
		return result

	# def dfs(self, row, col):
	# 	counter = 1
	# 	self.grid[row][col] = -1
	# 	if col + 1 < len(self.grid[0]) and self.grid[row][col + 1] == 1:
	# 		counter += self.dfs(row, col + 1)
	# 	if col - 1 >= 0 and self.grid[row][col - 1] == 1:
	# 		counter += self.dfs(row, col - 1)
	# 	if row + 1 < len(self.grid) and self.grid[row + 1][col] == 1:
	# 		counter += self.dfs(row + 1, col)
	# 	if row - 1 >= 0 and self.grid[row - 1][col] == 1:
	# 		counter += self.dfs(row - 1, col)
	# 	return counter

	def bfs(self, x, y):
		counter = 1
		queue = []
		queue.append((x, y))
		queueLen = len(queue)
		self.grid[x][y] = -1
		while queue:
			for _ in range(queueLen):
				row, col = queue.pop(0)
				if col + 1 < len(self.grid[0]) and self.grid[row][col + 1] == 1:
					self.grid[row][col + 1] = -1
					counter += 1
					queue.append((row, col + 1))
				if col - 1 >= 0 and self.grid[row][col - 1] == 1:
					self.grid[row][col - 1] = -1
					counter += 1
					queue.append((row, col - 1))
				if row + 1 < len(self.grid) and self.grid[row + 1][col] == 1:
					self.grid[row + 1][col] = -1
					counter += 1
					queue.append((row + 1, col))
				if row - 1 >= 0 and self.grid[row - 1][col] == 1:
					self.grid[row - 1][col] = -1
					counter += 1
					queue.append((row - 1, col))
			queueLen = len(queue)
		return counter



def main():
	island = [
	[0,0,1,0,0,0,0,1,0,0,0,0,0],
	[0,0,0,0,0,0,0,1,1,1,0,0,0],
	[0,1,1,0,1,0,0,0,0,0,0,0,0],
	[0,1,0,0,1,1,0,0,1,0,1,0,0],
	[0,1,0,0,1,1,0,0,1,1,1,0,0],
	[0,0,0,0,0,0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,0,1,1,0,0,0,0]
	]
	# island = [
	# [1, 0, 1],
	# [1, 1, 1]
	# ]
	print(Solution().maxAreaOfIsland(island))

if __name__ == "__main__":
	main()