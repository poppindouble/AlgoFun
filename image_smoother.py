class Solution:
	# def imageSmoother(self, M):
	# 	result = [[0 for col in M[0]] for row in M]
	# 	for x, row in enumerate(M):
	# 		for y, col in enumerate(row):
	# 			left = (x - 1, y)
	# 			leftUp = (x - 1, y - 1)
	# 			up = (x, y - 1)
	# 			rightUp = (x + 1, y - 1)
	# 			right = (x + 1, y)
	# 			rightDown = (x + 1, y + 1)
	# 			down = (x, y + 1)
	# 			leftDown = (x - 1, y + 1)
	# 			origin = (x, y)
	# 			allPoints = [left, leftUp, up, rightUp, right, rightDown, down, leftDown, origin]
	# 			available = filter(lambda x: x[0] < len(M) and x[0] >= 0 and x[1] < len(M[0]) and x[1] >= 0, allPoints)
	# 			availablePoint = list(map(lambda x: M[x[0]][x[1]], available))
	# 			result[x][y] = sum(availablePoint) / len(availablePoint)
	# 	return result

	def imageSmoother(self, M):
		dx, dy = [-1, 0, 1], [-1, 0, 1]
		w, h = len(M[0]), len(M)
		N = []
		for x in range(h):
			row = []
			for y in range(w):
				nbs = [M[x + i][y + j] for i in dx for j in dy if 0 <= x + i < h and 0 <= y + j < w]
				row.append(sum(nbs) // len(nbs))
			N.append(row)
		return N

def main():
	oldImage = [
	[1,1,1],
	[1,0,1],
	[1,1,1]
	]

	newImage = Solution().imageSmoother(oldImage)
	for row in newImage:
		print(row)

if __name__ == "__main__":
	main()