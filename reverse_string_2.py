class Solution:
	def reverseStr(self, s, k):
		result = ""
		for i in range(0, len(s), 2*k):
			tempStr = s[i : i+2*k]
			result += tempStr[0:k][::-1] + tempStr[k:]
		return result

def main():
	print(Solution().reverseStr("012345678901234567890123456789abcdekkk", 5))

if __name__ == "__main__":
	main()