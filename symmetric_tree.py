class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetric(self, root):
		return self.__isLeftRightEqual__(root, root)

	def __isLeftRightEqual__(self, tree1, tree2):
		if tree1 is None and tree2 is None:
			return True
		if tree1 and tree2 and tree1.val == tree2.val:
			return (
				self.__isLeftRightEqual__(tree1.left, tree2.right) and
				self.__isLeftRightEqual__(tree1.right, tree2.left)
				)
		else:
			return False

def main():

	root = TreeNode(1)
	node1 = TreeNode(2)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)
	node5 = TreeNode(4)
	node6 = TreeNode(3)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	# node2.right = node6

	print(Solution().isSymmetric(root))

if __name__ == "__main__":
	main()