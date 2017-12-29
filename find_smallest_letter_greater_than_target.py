class Solution:
	# def nextGreatestLetter(self, letters, target):
	# 	head = 0
	# 	tail = len(letters) - 1
	# 	while head <= tail:
	# 		middle = (head + tail) // 2
	# 		if letters[middle] == target:
	# 			middle += 1
	# 			while middle < len(letters):
	# 				if letters[middle] == letters[middle - 1]:
	# 					middle += 1
	# 				else:
	# 					return letters[middle]
	# 			return letters[0]
	# 		if letters[middle] < target:
	# 			head = middle + 1
	# 		if letters[middle] > target:
	# 			tail = middle - 1
	# 	if head <= len(letters) - 1:
	# 		return letters[head]
	# 	return letters[0]

	def nextGreatestLetter(self, letters, target):
		letters = set(map(ord, letters))
		for x in range(1, 27):
			candidate = ord(target) + x
			if candidate > ord('z'):
				candidate -= 26
			if candidate in letters:
				return chr(candidate)


def main():
	print(Solution().nextGreatestLetter(["c", "f", "j", "k", "k", "k"], "k"))

if __name__ == "__main__":
	main()