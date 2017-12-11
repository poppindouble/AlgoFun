class Solution:
	def containsDuplicate(self, nums):
		tempSet = set()
		for i in nums:
			if i not in tempSet:
				tempSet.add(i)
			else:
				return True
		return False

def main():
	print(Solution().containsDuplicate([2, 3, 4, 5, 1, 1]))

if __name__ == "__main__":
	main()