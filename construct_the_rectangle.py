import sys
from math import sqrt

class Solution:
	# def constructRectangle(self, area):
	# 	root = int(sqrt(area))
	# 	result = sys.maxsize
	# 	resultList = [0] * 2
	# 	for width in range(1,root + 1):
	# 		if area % width == 0:
	# 			height = area // width
	# 			if height - width < result:
	# 				result = height - width
	# 				resultList[0:2] = [width, height]
	# 	return resultList

	def constructRectangle(self, area):
		root = int(sqrt(area))
		L, W = area, 1
		for x in range(root, 0, -1):
			if area % x == 0:
				L, W = area // x, x
				break
		return [L, W]

def main():
	print(Solution().constructRectangle(546))

if __name__ == "__main__":
	main()