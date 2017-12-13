"""
下面的讨论对先拿者而言：

因为一次可以拿1~3个石头，所以n=1 ，2，3时候是必胜状态，因为你一次可以拿完。

而4是必败状态，因为你第一次无论拿 几块，对手都可以一次拿完。（你拿1块，对手拿3个；你拿2块，对手拿2块；你拿3块，对手拿1块）

而5，6，7则是必胜状态，因为你一次可以拿到剩下4个，让对手进入必败状态。

同理，8是必败状态，无论拿几个，对手都进入了5，6，7的必胜状态…..

9，10，11必胜，因为可以拿到剩下8块给对手,12为必败…….

总结：能被4整除的必败，否则必胜。
"""

class Solution:
	def canWinNim(self, n):
		return not n % 4 == 0
	# def canWinNim(self, n):
	# 	return self.__searchTree__(n, True)

	# def __searchTree__(self, n, myTurn):
	# 	if n <= 3 and not myTurn:
	# 		return False
	# 	if n <= 3 and myTurn:
	# 		return True
	# 	if myTurn:
	# 		return self.__searchTree__(n - 3, not myTurn) or self.__searchTree__(n - 2, not myTurn) or self.__searchTree__(n - 1, not myTurn)
	# 	else: 
	# 		return self.__searchTree__(n - 3, not myTurn) and self.__searchTree__(n - 2, not myTurn) and self.__searchTree__(n - 1, not myTurn)
def main():
	print(Solution().canWinNim(4))

if __name__ == "__main__":
	main()