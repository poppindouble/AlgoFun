class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	"""
	one wired case forget to consider in this style of code, if i input None
	the standard result is ""
	but my function will return "()"
	"""
	def tree2str(self, root):
		word = "()"
		if not root:
			return word
		left = self.tree2str(root.left)
		right = self.tree2str(root.right)
		if left == word and right == word:
			return str(root.val)
		elif left == word and right != word:
			return '{0}{1}({2})'.format(str(root.val), word, right)
		elif left != word and right == word:
			return '{0}({1})'.format(str(root.val), left)
		return '{0}({1})({2})'.format(str(root.val), left, right)

	def tree2str2(self, root):
		word = ""
		if not root:
			return word
		left = self.tree2str2(root.left)
		right = self.tree2str2(root.right)
		if left == word and right == word:
			return str(root.val)
		elif left == word and right != word:
			return '{0}({1})({2})'.format(str(root.val), word, right)
		elif left != word and right == word:
			return '{0}({1})'.format(str(root.val), left)
		return '{0}({1})({2})'.format(str(root.val), left, right)

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
	node1.right = node3
	# node1.left = node3
	# node1.right = node4
	# node2.left = node5
	# node2.right = node6
	# node3.left = node7
	# node7.right = node8

	print(Solution().tree2str(root))
	print(Solution().tree2str2(root))

if __name__ == "__main__":
	main()