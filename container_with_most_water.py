class Solution:
	def maxArea(self, height):
		i, j = 0, len(height) - 1
		result = -1
		while i < j:
			result = max(result, min(height[i], height[j]) * (j - i))
			if height[i] < height[j]:
				i += 1
			else:
				j -=1
		return result

def main():
	print(Solution().maxArea([5,2,7,4,9,10,2,4,8]))

if __name__ == "__main__":
	main()