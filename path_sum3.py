class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def pathSum(self, root, sum):
		ans = 0
		if not root:
			return 0
		ans = self.helper(root, sum)
		ans += self.pathSum(root.left, sum)
		ans += self.pathSum(root.right, sum)
		return ans


	def helper(self, root, sum):
		if not root:
			return 0
		result = 0
		if root.val == sum:
			result += 1
		left = self.helper(root.left, sum - root.val)
		right = self.helper(root.right, sum - root.val)
		return result + left + right

	def findAllThePathSum(self, root, sum):
		if not root:
			return []
		result = self.findPath(root, sum)
		left = self.findAllThePathSum(root.left, sum)
		right = self.findAllThePathSum(root.right, sum)
		return result + left + right

	def findPath(self, root, sum):
		if not root:
			return []
		if not root.left and not root.right and root.val == sum:
			return [[root.val]]
		res = []
		if sum == root.val:
			res = [[root.val]]
		left = self.findPath(root.left, sum - root.val)
		right = self.findPath(root.right, sum - root.val)
		temp = left + right
		return list(map(lambda x: [root.val] + x, temp)) + res

def main():
	root = TreeNode(10)
	node1 = TreeNode(5)
	node2 = TreeNode(-3)
	node3 = TreeNode(3)
	node4 = TreeNode(2)
	node5 = TreeNode(11)
	node6 = TreeNode(2)
	node7 = TreeNode(-2)
	node8 = TreeNode(1)
	node9 = TreeNode(8)

	node10 = TreeNode(0)
	node11 = TreeNode(0)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7
	node4.right = node8
	node8.left = node9

	node8.right = node10
	node10.right = node11
	
	num = 8
	print(Solution().pathSum(root, num))
	print(Solution().findAllThePathSum(root, num))

if __name__ == "__main__":
	main()