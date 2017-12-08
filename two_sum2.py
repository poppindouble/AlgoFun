class Solution():
	def twoSum(self, numbers, target):
		i, j = 0, len(numbers) - 1
		while i < j:
			if numbers[i] + numbers[j] == target:
				break
			if numbers[i] + numbers[j] < target:
				i += 1
			if numbers[i] + numbers[j] > target:
				j -= 1
		return (i + 1, j + 1)


def main():
	print(Solution().twoSum([2, 7, 8, 9, 11, 12, 14, 15, 20], 20))

if __name__ == "__main__":
	main()