import sys

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def getMinimumDifference(self, root):
		if not root:
			return
			
		ans = sys.maxsize
		node1 = root.left
		node2 = root.right
		while node1 and node1.right:
			node1 = node1.right
		while node2 and node2.left:
			node2 = node2.left
		if node1:
			ans = min(ans, root.val - node1.val)
		if node2:
			ans = min(ans, node2.val - root.val)

		leftMinimum = self.getMinimumDifference(root.left)
		if leftMinimum:
			ans = min(ans, leftMinimum)
		rightMinimum = self.getMinimumDifference(root.right)
		if rightMinimum:
			ans = min(ans, rightMinimum)
		return ans

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

	print(Solution().getMinimumDifference(root))

if __name__ == "__main__":
	main()