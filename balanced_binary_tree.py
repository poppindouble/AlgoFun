class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isBalanced(self, root):
		(result, _) = self.__isBalancedAndTreeHeight__(root)
		return result


	def __isBalancedAndTreeHeight__(self, root):
		if root is None:
			return (True, 0)
		(isLeftTreeBalanced, leftTreeHeight) = self.__isBalancedAndTreeHeight__(root.left)
		(isRightTreeBalanced, rightTreeHeight) = self.__isBalancedAndTreeHeight__(root.right)
		if (isLeftTreeBalanced and isRightTreeBalanced) and (abs(leftTreeHeight - rightTreeHeight) <= 1):
			return (True, max(leftTreeHeight, rightTreeHeight) + 1)
		else:
			return (False, 0)

def main():
	root = TreeNode(0)
	node1 = TreeNode(-3)
	node2 = TreeNode(9)
	node3 = TreeNode(-10)
	node4 = TreeNode(5)

	root.left = node1
	# root.right = node2
	node1.left = node3
	# node2.right = node4

	print(Solution().isBalanced(root))

if __name__ == "__main__":
	main()