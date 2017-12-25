import sys

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def findTarget(self, root, k):
		print(self.__helper__(root, set(), k))

	def __helper__(self, root, mySet, k):
		if not root:
			return (False, mySet)
		found = False
		leftFound, leftSet = self.__helper__(root.left, mySet, k)
		if k - root.val in leftSet:
			found = True
		leftSet.add(root.val)
		rightFound, rightSet = self.__helper__(root.right, leftSet, k)

		if found or rightFound or leftFound:
			return (True, rightSet)
		return (False, rightSet)


def main():

	root = TreeNode(6)
	node1 = TreeNode(2)
	node2 = TreeNode(8)
	node3 = TreeNode(0)
	node4 = TreeNode(4)
	node5 = TreeNode(7)
	node6 = TreeNode(9)
	node7 = TreeNode(3)
	node8 = TreeNode(5)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node4.left = node7
	node4.right = node8

	print(Solution().findTarget(root, 7))

if __name__ == "__main__":
	main()