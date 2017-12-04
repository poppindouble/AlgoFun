class Solution:
	def countAndSay(self, n):

		result = "1"
		for i in range(2, n + 1):
			result = self.__transform__(result)
		return result

	def __transform__(self, string):
		result = ""
		i, j = 0, 0
		counter = 0
		while j <= len(string):
			if j == len(string):
				result = result + "{}{}".format(counter, string[i])
				break
			if string[i] == string[j]:
				counter += 1
				j += 1
			else:
				result = result + "{}{}".format(counter, string[i])
				i = j
				counter = 0
		return result

def main():
	print(Solution().countAndSay(1))

if __name__ == "__main__":
	main()