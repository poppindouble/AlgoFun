class Solution:
	def containsNearbyDuplicate(self, nums, k):
		if k <= 0: return False
		tempSet = set()
		lastIndex = 0

		for index, num in enumerate(nums):
			if index > k: tempSet.remove(nums[lastIndex])
			if num in tempSet:
				return True
			tempSet.add(num)
			if index > k: lastIndex += 1
		return False

def main():
	print(Solution().containsNearbyDuplicate([3,2,1,6,3,8,6,3], 2))

if __name__ == "__main__":
	main()