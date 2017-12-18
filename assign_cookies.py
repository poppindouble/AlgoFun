class Solution:
	def findContentChildren(self, g, s):
		g = sorted(g)
		s = sorted(s)
		result = 0
		i = j = 0
		while i < len(g) and j < len(s):
			if s[j] >= g[i]:
				result += 1
				i += 1
			j += 1
		return result


def main():
	print(Solution().findContentChildren([2,4,5,8], [1,2,6,8,10]))

if __name__ == "__main__":
	main()