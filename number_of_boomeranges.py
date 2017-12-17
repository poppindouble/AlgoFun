"""
https://baike.baidu.com/item/%E6%8E%92%E5%88%97/7804523
"""

from collections import defaultdict

class Solution:
	def numberOfBoomerangs(self, points):
		result = 0
		for point1 in points:
			tempDict = defaultdict(int)
			for point2 in points:
				if point1 != point2:
					tempDict[pow((point1[0] - point2[0]), 2) + pow((point1[1] - point2[1]), 2)] += 1
			for _, val in tempDict.items():
				result += val * (val - 1)
		return result
def main():
	print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0], [0, 1], [-1, 0]]))

if __name__ == "__main__":
	main()