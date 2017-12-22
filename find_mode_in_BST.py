from collections import Counter

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def findMode(self, root):
		myDict = Counter(self.__helper__(root))
		mode = -1
		result = []
		for key, val in myDict.items():
			if val == mode:
				result.append(key)
			if val > mode:
				result.clear()
				result.append(key)
				mode = max(mode, val)
		return result

	def __helper__(self, root):
		if not root:
			return []
		return self.__helper__(root.left) + [root.val] + self.__helper__(root.right)

def main():

	root = TreeNode(6)
	node1 = TreeNode(4)
	node2 = TreeNode(8)
	node3 = TreeNode(0)
	node4 = TreeNode(4)
	node5 = TreeNode(7)
	node6 = TreeNode(9)
	node7 = TreeNode(4)
	node8 = TreeNode(5)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node4.left = node7
	node4.right = node8

	print(Solution().findMode(root))

if __name__ == "__main__":
	main()