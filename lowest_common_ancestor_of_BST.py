class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		if not root: return
		if q.val < p.val: (p, q) = (q, p)
		if root.val == p.val or root.val == q.val:
			return root
		if p.val < root.val and q.val > root.val:
			return root
		if root.val > q.val:
			return self.lowestCommonAncestor(root.left, p, q)
		if root.val < p.val:
			return self.lowestCommonAncestor(root.right, p, q)

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

	print(Solution().lowestCommonAncestor(root, node7, node3).val)

if __name__ == "__main__":
	main()