"""
tailing 0, can only be produced by 5 * 2
and the number of 2 is far more then 5
so the question become:
count 5s in prime factors.

let's say 18!
there is totally 3 5s which comes from 5, 10, 15
but let's say 25!
totally 5 5s which comes from
5, 10, 15, 20, 25,
but 25 is 5 * 5
so actually 6 5s
let's say 128!
5, 10, 15, 20, 25(5 * 5), 30, 35,
40, 45, 50(5 * 5 * 2), 55, 60, 65, 70, 75(5 * 5 * 3), 80,
85, 90, 95, 100(5 * 5 * 4), 105, 110, 115, 120, 125(5 * 5 * 5)
notice, 25, 50, 75, 100 give 2 5s at a time
and 125 gives 3 5s at a time
so 
result = (n / 5) + (n / 25) + (n / 125) + (n / 625) ....
"""

class Solution():
	def trailingZeros(self, n):
		result = 0
		x = 5
		while n // x:
			result = result + n // x
			x = x * 5
		return result

def main():
	print(Solution().trailingZeros(5))

if __name__ == "__main__":
	main()