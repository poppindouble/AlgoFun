class Solution:
	def guessNumber(self, n):
		head = 1
		tail = n
		while head <= tail:
			middle = (head + tail) // 2
			if self.guess(middle) == 0:
				return middle
			if self.guess(middle) == -1:
				head = middle + 1
			if self.guess(middle) == 1:
				tail = middle - 1
		print(head, tail)

	def guess(self, num):
		target = 6
		if num == target:
			return 0
		if num < target:
			return -1
		if num > target:
			return 1

def main():
	print(Solution().guessNumber(10))

if __name__ == "__main__":
	main()