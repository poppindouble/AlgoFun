"""
if len(A) >= len(B)
we need to double A size to make sure if B is in it
A = "abcd"
B = "cd"

if len(B) < len(A)
we need to add up A until len(A) > len(B)
A = "abcd"
B = "cdabcdab"

"""

class Solution:
	def repeatedStringMatch(self, A, B):
		temp = A[:]
		i = 1
		if len(A) >= len(B):
			while len(A) <= 2 * len(temp):
				if B in A:
					return i
				A += temp
				i += 1
			return -1
		else:
			while len(A) <= len(B) + len(temp):
				if B in A:
					return i
				A += temp
				i += 1
			return -1

	def repeatedStringMatch(self, A, B):
		temp = A[:]
		i = 1
		while len(A) <= 2 * max(len(A), len(B)):
			if B in A:
				return i
			A += temp
			i += 1
		return -1

def main():
	print(Solution().repeatedStringMatch("abcd", "cdabcdab"))

if __name__ == "__main__":
	main()