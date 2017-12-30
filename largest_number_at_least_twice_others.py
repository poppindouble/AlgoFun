class Solution:
	def dominantIndex(self, nums):
		first = -1
		second = -1
		result = -1
		for index, num in enumerate(nums):
			if num > first:
				first, second = num, first
				result = index
			elif second < num < first:
				second = num
		return result if first >= 2 * second else -1

def main():
	print(Solution().dominantIndex([3, 6, 1, 0]))

if __name__ == "__main__":
	main()