class Solution:
	def isIsomorphic(self, s, t):
		tempDic = {}
		tempSet = set()
		for i, j in zip(s, t):
			if i not in tempDic:
				if j not in tempSet:
					tempDic[i] = j
					tempSet.add(j)
				else:
					return False
			else:
				if tempDic[i] != j:
					return False
		return True

def main():
	print(Solution().isIsomorphic("abb", "egg"))

if __name__ == "__main__":
	main()