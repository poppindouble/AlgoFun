class Solution:
	def searchInsert(self, nums, target):
		head = 0
		tail = len(nums) - 1
		
		if target < nums[0]:
			return 0

		while head <= tail:
			middle = (head + tail) // 2
			if nums[middle] == target:
				return middle
			if nums[middle] > target:
				tail = middle - 1
			else:
				head = middle + 1

		return head


def main():
	print(Solution().searchInsert([1, 2, 5, 6], 7))

if __name__ == "__main__":
	main()