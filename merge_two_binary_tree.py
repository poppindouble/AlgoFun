class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# def mergeTrees(self, t1, t2):
		# result = 0
		# temp = TreeNode(0)
		# if not t1 and not t2:
		# 	return None
		# elif t1 and not t2:
		# 	result = t1.val
		# 	temp.left = self.mergeTrees(t1.left, None)
		# 	temp.right = self.mergeTrees(t1.right, None)
		# elif not t1 and t2:
		# 	result = t2.val
		# 	temp.left = self.mergeTrees(None, t2.left)
		# 	temp.right = self.mergeTrees(None, t2.right)
		# else:
		# 	result = t1.val + t2.val
		# 	temp.left = self.mergeTrees(t1.left, t2.left)
		# 	temp.right = self.mergeTrees(t1.right, t2.right)
		# temp.val = result
		# return temp

	def mergeTrees(self, t1, t2):
		if not t1:
			return t2
		if not t2:
			return t1
		t1.left = self.mergeTrees(t1.left, t2.left)
		t1.right = self.mergeTrees(t1.right, t2.right)
		t1.val += t2.val
		return t1

	def print(self, root):
		if not root:
			return
		print(root.val)
		self.print(root.right)
		self.print(root.left)
	

def main():
	root = TreeNode(0)
	node1 = TreeNode(1)
	node2 = TreeNode(2)
	node3 = TreeNode(3)
	node6 = TreeNode(6)
	node7 = TreeNode(7)
	node8 = TreeNode(8)

	root.left = node1
	root.right = node2
	node1.left = node3
	node2.right = node6
	node3.left = node7
	node7.right = node8

	root2 = TreeNode(1)
	node4 = TreeNode(4)
	node5 = TreeNode(5)
	root2.left = node4
	node4.right = node5

	s = Solution()
	s.print(s.mergeTrees(root, root2))

if __name__ == "__main__":
	main()