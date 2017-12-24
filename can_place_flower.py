class Solution:
	# def canPlaceFlowers(self, flowerbed, n):
	# 	i = 0
	# 	result = 0
	# 	while i < len(flowerbed):
	# 		digit = flowerbed[i]
	# 		if digit == 0:
	# 			left = None if i - 1 < 0 else i - 1
	# 			right = None if i + 1 >= len(flowerbed) else i + 1
	# 			if left == None and right == None:
	# 				result = 1 - flowerbed[i]
	# 				break
	# 			elif left == None and flowerbed[right] == 0:
	# 				flowerbed[i] = 1
	# 				result += 1
	# 			elif right == None and flowerbed[left] == 0:
	# 				flowerbed[i] = 1
	# 				result += 1
	# 			elif left != None and right != None:
	# 				if flowerbed[left] == 0 and flowerbed[right] == 0:
	# 					flowerbed[i] = 1
	# 					result += 1
	# 				print(result)
	# 		i += 1
	# 	print(flowerbed)
	# 	return result >= n

	def canPlaceFlowers(self, flowerbed, n):
		result = 0
		for index, val in enumerate(flowerbed):
			if val: continue
			if index > 0 and flowerbed[i - 1]: continue
			if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
			result += 1
			flowerbed[i] = 1
		return result >= n


def main():
	print(Solution().canPlaceFlowers([1,0,0,0,0,1], 1))

if __name__ == "__main__":
	main()