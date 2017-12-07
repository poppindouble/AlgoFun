class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sortedArrayToBST(self, nums):
		if not nums:
			return None

		middle = len(nums) // 2
		root = TreeNode(nums[middle])
		root.left = self.sortedArrayToBST(nums[0:middle])
		root.right = self.sortedArrayToBST(nums[middle+1:])
		return root

def traverseTree(root):
	result = []
	queue = [root]
	layerLenth = len(queue)

	while queue:
		temp = []
		for _ in range(layerLenth):
			node = queue[0]
			queue = queue[1:]
			if node:
				temp.append(node.val)
				queue.append(node.left)
				queue.append(node.right)
			else:
				temp.append(None)
		layerLenth = len(queue)
		result.append(temp)
	print(result)
	return result
			

def main():
	root = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
	result = traverseTree(root)



if __name__ == "__main__":
	main()