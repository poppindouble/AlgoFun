class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def trimBST(self, root, L, R):
		if not root:
			return None
		left = self.trimBST(root.left, L, R)
		right = self.trimBST(root.right, L, R)
		if root.val < L:
			return right
		if root.val > R:
			return left
		temp = TreeNode(root.val)
		temp.left = left
		temp.right = right
		return temp
			

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

	print(Solution().trimBST(root, 5, 7))

if __name__ == "__main__":
	main()