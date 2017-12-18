"""
for each house, we need to find out where to insert it into the heater
bisect.bisect_right will give you the right most indext to insert into the array and keep the order same
bisect.bisect_left will give you the left most index to insert into the array and keep the order same
we can use binary search to do it, like my method
or use the build in lib, which is bisect
for each house, find out the minimum of left and right
and find the max of all these minimum value
"""

import bisect
import sys

class Solution:
	# def findRadius(self, houses, heaters):
	# 	result = -sys.maxsize - 1
	# 	for house in houses:
	# 		right, left = self.findInsertionPosition(house, heaters)
	# 		if left < 0:
	# 			result = max(result, heaters[right] - house)
	# 		elif right >= len(heaters):
	# 			result = max(result, house - heaters[left])
	# 		else:
	# 			temp = min(heaters[right] - house, house - heaters[left])
	# 			result = max(temp, result)
	# 	print(result)
	# 	return result

	# def findInsertionPosition(self, house, heaters):
	# 	head = 0
	# 	tail = len(heaters) - 1
	# 	while head <= tail:
	# 		middle = (head + tail) // 2
	# 		if heaters[middle] == house:
	# 			return (middle, middle)
	# 		if heaters[middle] > house:
	# 			tail = middle - 1
	# 		if heaters[middle] < house:
	# 			head = middle + 1
	# 	return (head, tail)

	def findRadius(self, houses, heaters):
		heaters = sorted(heaters)
		result = -sys.maxsize - 1
		for house in houses:
			leftDistance = rightDistance = sys.maxsize
			rightMostIndex = bisect.bisect_right(heaters, house)
			if rightMostIndex > 0:
				leftDistance = house - heaters[rightMostIndex - 1]
			leftMostIndex = bisect.bisect_left(heaters, house)
			if leftMostIndex < len(heaters):
				rightDistance = heaters[leftMostIndex] - house
			result = max(result, min(rightDistance, leftDistance))
		print(result)
		return result

def main():
	Solution().findRadius([4, 10, 14, 25, 30, 35], [1, 3, 5, 8, 10, 13, 22, 25, 29, 30, 31])

if __name__ == "__main__":
	main()