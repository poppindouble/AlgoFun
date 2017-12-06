"""
let's see an example:
if n = 1
we only have one way 
1 step

if n = 2
we have two ways:
2 steps
1 step + 1 steps

if n = 3
we have three ways:
1 step + 2 steps

2 steps + 1 step
1 step + 1 step + 1 step

if n = 4
we have five ways:
2 steps + 2 steps
1 step + 1 step + 2 steps

1 step + 2 steps + 1 step
2 steps + 1 step + 1 step
1 step + 1 step + 1 step

so:
f(n) = f(n - 1) + f(n - 2)
which means the ways to walk to nth floor
only in one of the situation
at f(n - 1) + 1 step
or
at f(n - 2) + 2 steps
well remember
f(n - 2) + 1 step + 1 step
is the same as
f(n - 1) + 1 step

so
f(n) = f(n - 1) + f(n -2)

-----------------
but the implementation might be out of time limited when we are doing top -> bottom -> top
we can start from bottom -> top

"""


class Solution:
	# def climbStairs(self, n):
	# 	if n == 1:
	# 		return 1
	# 	if n == 2:
	# 		return 2
	# 	return self.climbStairs(n - 1) + self.climbStairs(n - 2)

	def climbStairs(self, n):
		if n == 1:
			return 1
		if n == 2:
			return 2

		i, j = 1, 2
		result = 0
		for _ in range(3, n + 1):
			result = i + j
			i = j
			j = result
		return result

def main():
	print(Solution().climbStairs(9))

if __name__ == "__main__":
	main()