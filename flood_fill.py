class Solution:
	def floodFill(self, image, sr, sc, newColor):
		if image[sr][sc] == newColor:
			return image
		temp = image[sr][sc]
		image[sr][sc] = newColor
		deltaX = deltaY = [-1, 0, 1]
		for i, j in [(x, y) for x in deltaX for y in deltaY]:
			if (0 <= sr + i < len(image)
			and 0 <= sc + j < len(image[0]) 
			and image[sr + i][sc + j] == temp 
			and abs(i) + abs(j) != 2):
				image = self.floodFill(image, sr + i, sc + j, newColor)
		return image

def main():
	# image = [
	# [1,1,1],
	# [1,1,0],
	# [1,0,1]
	# ]
	image = [
	[0,0,0],
	[0,1,1]
	]
	newImage = Solution().floodFill(image, 1, 1, 1)
	for row in newImage:
		print(row)

if __name__ == "__main__":
	main()
