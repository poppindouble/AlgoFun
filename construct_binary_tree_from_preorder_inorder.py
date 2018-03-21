class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if len(inorder) == 0:
        return None
    root = TreeNode(preorder[0])
    leftInorder = inorder[0 : inorder.index(root.val)]
    rightInorder = inorder[inorder.index(root.val)+1 : ]

    leftPreorder = preorder[1 : 1+len(leftInorder)]
    rightPreorder = preorder[1+len(leftInorder) : ]
    root.left = buildTree(leftPreorder, leftInorder)
    root.right = buildTree(rightPreorder, rightInorder)
    return root

root = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

# print(root.val)
# print(root.left.val)
# print(root.right.val)
# print(root.right.left.val)
# print(root.right.right.val)

def preorder(root):
    if not root:
        return []
    result = [root.val]
    left = preorder(root.left)
    right = preorder(root.right)
    return result + left + right

print(preorder(root))