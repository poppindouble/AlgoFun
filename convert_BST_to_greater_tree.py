"""
Three traverse structure:

1. left middle right(inorder)
def dfsLeftMiddleRight(root):
	if not root:
		return None
	# recurse left child first
	self.dfsLeftMiddleRight(root.left)
	# do something about your root
	root.val += 1
	# ecurse right child
	self.dfsLeftMiddleRight(root.right)

2.  middle left right(preorder)
def dfsMiddleLeftRight(root):
	if not root:
		return None
	# do something about your root
	root.val += 1
	# recurse left child
	self.dfsMiddleLeftRight(root.left)
	# recurse right child first
	self.dfsMiddleLeftRight(root.right)

3.  left right middle(preorder)
def dfsLeftRightMiddle(root):
	if not root:
		return None
	# recurse left child
	self.dfsLeftRightMiddle(root.left)
	# recurse right child first
	self.dfsLeftRightMiddle(root.right)
	# do something about your root
	root.val += 1
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def convertBST(self, root):
		self.__helper__(root, 0)
		self.__print__(root)

	def __print__(self, root):
		if not root:
			return
		self.__print__(root.right)
		print(root.val)
		self.__print__(root.left)

	def __helper__(self, root, acc):
		if not root:
			return acc
		newAcc = self.__helper__(root.right, acc)
		root.val += newAcc
		newAcc = root.val
		return self.__helper__(root.left, newAcc)

def main():

	root = TreeNode(18)
	node1 = TreeNode(10)
	node2 = TreeNode(30)
	node3 = TreeNode(8)
	node4 = TreeNode(15)
	node5 = TreeNode(22)
	node6 = TreeNode(50)
	node7 = TreeNode(7)
	node8 = TreeNode(9)
	node9 = TreeNode(16)
	node10 = TreeNode(19)
	node11 = TreeNode(28)
	node12 = TreeNode(37)
	node13 = TreeNode(80)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node3.left = node7
	node3.right = node8
	node4.right = node9
	node5.left = node10
	node5.right = node11
	node6.left = node12
	node6.right = node13

	print(Solution().convertBST(root))

if __name__ == "__main__":
	main()