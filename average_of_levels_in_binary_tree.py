class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def averageOfLevels(self, root):
		result = []
		queue = [root]
		while queue:
			result.append(sum([n.val for n in queue]) / len(queue))
			newQueue = []
			for n in queue:
				if n.left: newQueue.append(n.left)
				if n.right: newQueue.append(n.right)
			queue = newQueue
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

	print(Solution().averageOfLevels(root))

if __name__ == "__main__":
	main()