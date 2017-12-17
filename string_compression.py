class Solution:
	# def compress(self, chars):
	# 	i = j = 0
	# 	counter = 0
	# 	while j < len(chars):
	# 		if chars[i] == chars[j]:
	# 			counter += 1
	# 			j += 1
	# 			continue
	# 		i += 1	
	# 		if counter > 1:
	# 			chars[i:i + len(str(counter))] = list(str(counter))
	# 			i += len(str(counter))
	# 		chars[i] = chars[j]
	# 		counter = 0
	# 	if counter > 1:
	# 		chars[i + 1:i + 1 + len(str(counter))] = list(str(counter))
	# 		print(chars)
	# 		return i + 1 + len(str(counter))
	# 	print(chars)
	# 	return i + 1

	def compress(self, chars):
		anchor = write = 0
		for read, c in enumerate(chars):
			if read + 1 == len(chars) or chars[read + 1] != c:
				chars[write] = chars[anchor]
				write += 1
				if read > anchor:
					for digit in str(read - anchor + 1):
						chars[write] = digit
						write += 1
				anchor = read + 1
		return write


def main():
	print(Solution().compress(["a","a","a","a","a","a","a","a","a","a","a","a", "z", "b","b","c","c","c","e"]))
	print(Solution().compress(["a","a","b","b","c","c","c"]))
	print(Solution().compress(["a"]))

if __name__ == "__main__":
	main()