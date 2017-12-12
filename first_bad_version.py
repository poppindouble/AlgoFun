class Solution:
	def firstBadVersion(self, n):
		head = 1
		tail = n

		while head <= tail:
			middle = (head + tail) // 2
			if self.isBadVersion(middle):
				tail = middle - 1
			else:
				head = middle + 1
		return head

	def isBadVersion(self, index):
		n = [False, False, False, False, True, True, True]
		return n[index - 1]

def main():
	print(Solution().firstBadVersion(7))

if __name__ == "__main__":
	main()