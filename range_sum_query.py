class NumArray:

	def __init__(self, nums):
		self.nums = nums
		self.sums = [0] * len(nums)
		result = 0
		for i in range(len(nums)):
			result += nums[i]
			self.sums[i] = result

	def sumRange(self, i, j):
		return self.sums[j] - self.sums[i] + self.nums[i]

def main():
	myArray = NumArray([-2, 0, 3, -5, 2, -1])
	print(myArray.sumRange(2, 5))

if __name__ == "__main__":
	main()