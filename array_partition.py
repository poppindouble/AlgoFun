class Solution:
	def arrayPairSum(self, nums):
		return sum(sorted(nums)[0::2])

def main():
	print(Solution().arrayPairSum([1,4,3,2]))

if __name__ == "__main__":
	main()