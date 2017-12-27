"""
if you wanna use root.left.val or root.right.val.
the terminate conditional should be 
if not root.left
	return -1
if not root.right
	return -1

for this quesiton,
we are sure the root is the smallest value
we only care about the branch where the left or right value whose value is not root value
as long as it is different from root.val, that val might be a potential answer
so we check left and right of every root
if the val is different from root.val
we just return that different val

so we will only reach the leaf when it is the minimum value form root all the way down to leaf
so when it reach to leaf, we can only return -1
means we can not find second minimum value, cuz it is roots anyways
if left or right is -1,
then we want the max of left and right, so it is either -1 or potential second minimum
if left and right both are not -1, then find the maximum, because you have two potential answer now
"""


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def findSecondMinimumValue(self, root):
		if not root:
			return -1
		left = self.findSecondMinimumValue(root.left) if root.val == root.left.val else root.left.val
		right = self.findSecondMinimumValue(root.right) if root.val == root.right.val else root.right.val
		if left == right == -1:
			return -1
		if left == -1 or right == -1:
			return max(left, right)
		return min(left, right)

def main():
	root = TreeNode(2)
	node1 = TreeNode(2)
	node2 = TreeNode(3)
	node3 = TreeNode(2)
	node4 = TreeNode(4)
	node5 = TreeNode(7)
	node6 = TreeNode(3)
	node7 = TreeNode(2)
	node8 = TreeNode(8)

	root.left = node1
	root.right = node2
	node1.left = node3
	node1.right = node4
	node2.left = node5
	node2.right = node6
	node3.left = node7
	node8.right = node8

	print(Solution().findSecondMinimumValue(root))

if __name__ == "__main__":
	main()