class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def hasPathSum(self, root, sum):
		if root is None:
			return False
		if (root.left is None) and (root.right is None):
			return sum == root.val
		if root.left is None:
			return self.hasPathSum(root.right, sum - root.val)
		if root.right is None:
			return self.hasPathSum(root.left, sum - root.val)
		return (self.hasPathSum(root.left, sum - root.val)) or (self.hasPathSum(root.right, sum - root.val))

def main():
	root = TreeNode(5)
	node1 = TreeNode(4)
	node2 = TreeNode(8)
	node3 = TreeNode(11)
	node4 = TreeNode(13)
	node5 = TreeNode(4)
	node6 = TreeNode(7)
	node7 = TreeNode(2)
	node8 = TreeNode(1)

	root.left = node1
	root.right = node2
	node1.left = node3
	node2.left = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7
	node5.right = node8

	print(Solution().hasPathSum(root, 22))

if __name__ == "__main__":
	main()