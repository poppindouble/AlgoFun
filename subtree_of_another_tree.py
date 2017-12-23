class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSubtree(self, s, t):
		if not s:
			return False
		return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.isSameTree(s, t)

	def isSameTree(self, s, t):
		if not s and not t:
			return True
		if s and t and s.val == t.val:
			return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
		return False

def main():
	root = TreeNode(3)
	node1 = TreeNode(4)
	node2 = TreeNode(5)
	node3 = TreeNode(1)
	node4 = TreeNode(2)
	node5 = TreeNode(0)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node3.left = node5

	root2 = TreeNode(4)
	node21 = TreeNode(1)
	node22 = TreeNode(2)
	root2.left = node21
	root2.right = node22

	print(Solution().isSubtree(root, root2))

if __name__ == "__main__":
	main()