"""
if p == None and q == None:
	return True
if p and q and p.val == q.val:

this is how to make sure p and q both is not empty,
the only situation it will goes to else is that one of p and q will be None
then we just return False

"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class Solution:
	def isSameTree(self, p, q):
		if p == None and q == None:
			return True
		if p and q and p.val == q.val:
			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
		else:
			return False


def main():
	p = TreeNode(3)
	node1 = TreeNode(4)
	node2 = TreeNode(5)
	node3 = TreeNode(6)
	node4 = TreeNode(7)
	node5 = TreeNode(8)

	p.left = node1
	p.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5

	q = TreeNode(3)
	node6 = TreeNode(4)
	node7 = TreeNode(5)
	node8 = TreeNode(6)
	node9 = TreeNode(7)
	node10 = TreeNode(8)

	q.left = node6
	q.right = node7
	node6.left = node8
	# node6.right = node9
	# node7.left = node10


	print(Solution().isSameTree(p, q))

if __name__ == "__main__":
	main()