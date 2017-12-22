class Solution:
	def checkRecord(self, s):
		counter = 0
		for char in s:
			if char == 'L':
				counter = 0
			if char == 'A':
				return False
			if char == 'L':
				counter += 1
				if counter == 2:
					return False
		return True