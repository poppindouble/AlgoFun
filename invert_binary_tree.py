class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def invertTree(self, root):
		if not root:
			return
		root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
		return root

def treeToArray(root):
	result = []
	queue = [root]
	layerLength = len(queue)

	while queue:
		for i in range(layerLength):
			node = queue.pop(0)
			result.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		layerLength = len(queue)

	return result

def main():
	root = TreeNode(3)
	node1 = TreeNode(4)
	node2 = TreeNode(5)
	node3 = TreeNode(6)
	node4 = TreeNode(7)
	node5 = TreeNode(8)
	node6 = TreeNode(4)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	
	newRoot = Solution().invertTree(root)
	print(treeToArray(newRoot))

if __name__ == "__main__":
	main()