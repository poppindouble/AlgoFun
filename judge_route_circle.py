class Solution:
	def judgeCircle(self, moves):
		x = 0
		y = 0
		for char in moves:
			if char == 'U':
				y += 1
			elif char == 'D':
				y -= 1
			elif char == 'L':
				x -= 1
			else:
				x += 1
		if x == 0 and y == 0:
			return True
		return False

def main():
	print(Solution().judgeCircle("UDLLRR"))

if __name__ == "__main__":
	main()