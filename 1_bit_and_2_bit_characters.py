class Solution:
	def isOneBitCharacter(self, bits):
		if len(bits) == 0:
			return False
		if len(bits) == 1:
			return bits[0] == 0
		double = single = False
		if bits[0:2] == [1, 0] or bits[0:2] == [1, 1]:
			double = self.isOneBitCharacter(bits[2:])
		if bits[0] == 0:
			single = self.isOneBitCharacter(bits[1:])
		return double or single

def main():
	print(Solution().isOneBitCharacter([1, 0, 0]))

if __name__ == "__main__":
	main()