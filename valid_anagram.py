class Solution:
	def isAnagram(self, s, t):
		dic = {}

		for char in s:
			dic[char] = (dic[char] + 1) if char in dic else 1

		for char in t:
			if char not in dic: return False
			dic[char] -= 1
			if dic[char] < 0: return False

		for _, val in dic.items():
			if val != 0: return False
		return True

def main():
	print(Solution().isAnagram("anagram", "nagaram"))
 

if __name__ == "__main__":
	main()