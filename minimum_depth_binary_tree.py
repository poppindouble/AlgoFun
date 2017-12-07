"""
The question is saying the number of nodes to leaf
so four situation:
the node is a leaf
the node left branch is None, so return the right branch depth
the node right branch is None, so return the left branch depth
the node has both branch, return min of both side
"""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def minDepth(self, root):
		if root is None:
			return 0
		if (root.left is None) and (root.right is None):
			return 1
		if root.left is None:
			return 1 + self.minDepth(root.right)
		if root.right is None:
			return 1 + self.minDepth(root.left)

		return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

def main():
	root = TreeNode(1)
	node1 = TreeNode(1)
	node2 = TreeNode(1)
	node3 = TreeNode(1)
	node4 = TreeNode(1)
	node5 = TreeNode(1)
	node6 = TreeNode(1)
	node7 = TreeNode(1)
	node8 = TreeNode(1)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node3.left = node7
	node7.right = node8

	print(Solution().minDepth(root))

if __name__ == "__main__":
	main()