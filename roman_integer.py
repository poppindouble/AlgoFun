class Solution:
	def romanToInt(self, s):
		dic = {
		'I' : 1,
		'V' : 5,
		'X' : 10,
		'L' : 50,
		'C' : 100,
		'D' : 500,
		'M' : 1000
		}

		result = 0
		previouseChar = ''
		# you can also use s[::-1] to reverse a list
		for val in reversed(s):
			result = self.__calculation__(result, val, previouseChar, dic)
			previouseChar = val

		return result

	def __calculation__(self, result, char, previouseChar, dic):
		if previouseChar == '':
			return result + dic[char]
		result = result - dic[char] if dic[char] < dic[previouseChar] else result + dic[char]
		return result


def main():
	print(Solution().romanToInt('MCMLIV'))

if __name__ == "__main__":
	main()