class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

node0 = RandomListNode(0)
node1 = RandomListNode(1)
node2 = RandomListNode(2)
node3 = RandomListNode(3)
node4 = RandomListNode(4)
node5 = RandomListNode(5)

node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node0.random = node2
node1.random = node0
node2.random = node2
node3.random = None
node4.random = node5
node5.random = node3

def copyRandomList(head):
    if not head:
        return None
    projection = {}
    temp = head
    while temp:
        if temp not in projection:
            current = RandomListNode(temp.label)
            projection[temp] = current
        if temp.next not in projection and temp.next:
            nextNode = RandomListNode(temp.next.label)
            projection[temp.next] = nextNode
        if temp.random not in projection and temp.random:
            randomNode = RandomListNode(temp.random.label)
            projection[temp.random] = randomNode

        if temp.next:
            projection[temp].next = projection[temp.next]
        if temp.random:
            projection[temp].random = projection[temp.random]
        temp = temp.next

    return projection[head]

temp = node0
while temp:
    print(temp.label, temp.random.label if temp.random else "None")
    temp = temp.next

print("++++++++++++++")

newHead = copyRandomList(node0)
temp = newHead
while temp:
    print(temp.label, temp.random.label if temp.random else "None")
    temp = temp.next
