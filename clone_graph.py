class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)

node0.neighbors = [node1, node2]
node1.neighbors = [node2]
node2.neighbors = [node2]

def serialized(root):
    visited = {}
    result = ""
    queue = []
    if not root:
        return ""
    queue.append(root)
    visited[root] = True
    while queue:
        curr = queue.pop()
        result += str(curr.label)
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)
                result += "," + str(neighbor.label)
            else:
                result += "," + str(neighbor.label)
        result += "#"
    return result

# visited 就是一个标识符，表示的是否已经创建了这个对象了
def bfs(root):
    visited = {}
    queue = []
    if not root:
        return None
    queue.append(root)
    newHead = UndirectedGraphNode(root.label)
    visited[root] = newHead
    while queue:
        curr = queue.pop()
        for neighbor in curr.neighbors:
            if neighbor not in visited:
                copy = UndirectedGraphNode(neighbor.label)
                visited[neighbor] = copy
                visited[curr].neighbors.append(copy)
                queue.append(neighbor)
            else:
                visited[curr].neighbors.append(visited[neighbor])
    return root

def dfs(root, visited):
    if not root:
        return visited
    newHead = UndirectedGraphNode(root.label)
    visited[root] = newHead
    for neighbor in root.neighbors:
        if neighbor not in visited:
            copy = UndirectedGraphNode(neighbor.label)
            visited[neighbor] = copy
            newHead.neighbors.append(dfs(neighbor, visited))
        else:
            newHead.neighbors.append(visited[neighbor])
    return newHead

def dfs2(root):
    if not root:
        return None
    return dfs2Help(root, {})

def dfs2Help(root, visited):
    if root in visited:
        return visited[root]
    copy = UndirectedGraphNode(root.label)
    visited[root] = copy
    for neighbor in root.neighbors:
        copy.neighbors.append(dfs2Help(neighbor, visited))
    return copy


print(serialized(node0))
newRoot = bfs(node0)
print(serialized(newRoot))

newRoot = dfs(node0, {})
print(serialized(newRoot))

newRoot = dfs2(node0)
print(serialized(newRoot))


