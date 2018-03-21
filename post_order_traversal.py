class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def postOrder(root):
    if not root:
        return None
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:
        temp = stack1.pop()
        if temp.left:
            stack1.append(temp.left)
        if temp.right:
            stack1.append(temp.right)
        stack2.append(temp)
    result = ""
    while stack2:
        result += str(stack2.pop().val)
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
    node2.right = node6
    node6.left = node5
    
    print(postOrder(root))

if __name__ == "__main__":
    main()