"""
we need to decided each number in this array
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ....., n - 1]
construct an array
[False, False, True, True, True, True, Ture, ...., True]
the first two are False, because we know 0, and 1 doesn't count

so, we start from 2
because 2 is a prime
we know 4, 6, 8, 10, ......
is not prime, we can mark them as False

we start from 3
because 3 is a prime
we know 6(marked by 2 as False), 9, 12, 15.....
is not prime, we can mark them as False

we start from 4, it is makred by 2 as False

we start from 5
because 5 is a prime
we know 10(marked by 2 as False), 15(marked by 3 as False)
20(makred by 2 as False), 25, 30(makred by 2 as False)
35........

we can noticed that if isPrime[i] is True, our start point gonna
be i * i

so if our {i * i >= n} we can stop
which means: i > sqrt(n) we can stop
so i in range(2, sqrt(n) + 1)

one good trick about python is that:
you can set bunch of array element using index slicing
"""


class Solution:
	def countPrimes(self, n):
		if n <= 2: return 0
		isPrime = [True] * n
		isPrime[0] = isPrime[1] = False
		for i in range(2, int(n ** 0.5) + 1):
			if isPrime[i]:
				isPrime[i * i:n:i] = [False] * len(isPrime[i * i:n:i])
		return sum(isPrime)

def main():
	print(Solution().countPrimes(36))

if __name__ == "__main__":
	main()