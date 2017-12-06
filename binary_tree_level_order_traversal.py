"""
classic BFS
"""

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def levelOrderBottom(self, root):
		result = []
		queue = [root]
		layerLength = len(queue)

		while len(queue):
			temp = []
			for i in range(layerLength):
				node = queue[0]
				queue = queue[1:]
				temp.append(node.val)

				if node.left is not None:
					queue.append(node.left)
				if node.right is not None:
					queue.append(node.right)
			layerLength = len(queue)
			# insert i 5x times faster then using +
			result.insert(0, temp)
		print(result)
		return result
		

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

	Solution().levelOrderBottom(root)

if __name__ == "__main__":
	main()