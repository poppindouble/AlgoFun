class Solution:
	def judgeSquareSum(self, c):
		head = 0
		tail = int(c ** 0.5)
		while head <= tail:
			if head ** 2 + tail ** 2 == c:
				return True
			if head ** 2 + tail ** 2 < c:
				head += 1
			else:
				tail -= 1
		return False


def main():
	print(Solution().judgeSquareSum(881))

if __name__ == "__main__":
	main()