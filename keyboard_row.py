class Solution:
	def findWords(self, words):
		keyboards = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
		return list(filter(lambda x: any(map(lambda y: set(x.lower()).issubset(y), keyboards)), words))

def main():
	print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))

if __name__ == "__main__":
	main()