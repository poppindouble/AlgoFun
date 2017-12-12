class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def binaryTreePaths(self, root):
		if not root: return []
		if not root.left and not root.right: return [str(root.val)]
		leftPath = self.binaryTreePaths(root.left)
		rightPath = self.binaryTreePaths(root.right)
		return list(map(lambda s: str(root.val) + "->" + s, leftPath)) + list(map(lambda s: str(root.val) + "->" + s, rightPath)) 
	

def main():
	root = TreeNode(0)
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node4 = TreeNode(4)
	node5 = TreeNode(5)
	node6 = TreeNode(6)
	node7 = TreeNode(7)
	node8 = TreeNode(8)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node3.left = node7
	node7.right = node8

	print(Solution().binaryTreePaths(root))

if __name__ == "__main__":
	main()