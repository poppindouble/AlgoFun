class Solution:
	def mySqrt(self, x):
		head = 1
		tail = x

		while head <= tail:
			mid = (head + tail) // 2
			if mid * mid == x:
				return mid
			if mid * mid > x:
				tail = mid - 1
			else:
				head = mid + 1
		return tail

def main():
	print(Solution().mySqrt(102923))

if __name__ == "__main__":
	main()