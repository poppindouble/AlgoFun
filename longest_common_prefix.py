class Solution:
	def longestCommonPrefix(self, strs):
		if len(strs) == 0:
			return ""
		result = strs[0]
		for str in strs[1:]:
			result = self.__findCommonPrefixOfTwoString__(result, str)
		return result


	def __findCommonPrefixOfTwoString__(self, str1, str2):
		result = ""
		if len(str1) > len(str2):
			(str2, str1) = (str1, str2)
		for index, char in enumerate(str1):
			if char == str2[index]:
				result += char
			else:
				break
		return result

def main():
	print(Solution().longestCommonPrefix(["aca","cba"]))

if __name__ == "__main__":
	main()