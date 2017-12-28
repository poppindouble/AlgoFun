class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# def longestUnivaluePath(self, root):
	# 	return self.__helper__(root)[1]

	# def __helper__(self, root):
		# if not root:
		# 	return (0, 0)
		# (leftCount, leftMax) = self.__helper__(root.left)
		# (rightCount, rightMax) = self.__helper__(root.right)
		# leftCount = leftCount + 1 if root.left and root.left.val == root.val else 0
		# rightCount = rightCount + 1 if root.right and root.right.val == root.val else 0
		# return(max(leftCount, rightCount), max(leftCount + rightCount, leftMax, rightMax))

	def longestUnivaluePath(self, root):
		if not root:
			return 0
		return(max(self.__helper__(root.left, root.val) + self.__helper__(root.right, root.val), self.longestUnivaluePath(root.left), self.longestUnivaluePath(root.right)))

	def __helper__(self, root, val):
		if not root or root.val != val:
			return 0
		left = self.__helper__(root.left, val)
		right = self.__helper__(root.right, val)
		return max(left, right) + 1

def main():
	root = TreeNode(0)
	node1 = TreeNode(3)
	node2 = TreeNode(0)
	node3 = TreeNode(3)
	node4 = TreeNode(3)
	node5 = TreeNode(0)
	node6 = TreeNode(0)
	node7 = TreeNode(3)
	node8 = TreeNode(3)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node3.left = node7
	node7.right = node8

	print(Solution().longestUnivaluePath(root))


if __name__ == "__main__":
	main()