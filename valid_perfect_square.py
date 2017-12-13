class Solution:
	def isPerfectSquare(self, num):
		head = 0
		tail = num
		while head <= tail:
			middle = (head + tail) // 2
			if middle * middle == num:
				return True
			if middle * middle > num:
				tail = middle - 1
			if middle * middle < num:
				head = middle + 1
		return False

def main():
	print(Solution().isPerfectSquare(3))

if __name__ == "__main__":
	main()