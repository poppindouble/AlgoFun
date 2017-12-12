class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def deleteNode(self, node):
		if not node.next:
			node = None
			return
		temp = node.next
		node.val = temp.val
		node.next = temp.next
		temp.next = None


def main():
	head = ListNode(0)
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node4 = ListNode(4)
	node5 = ListNode(5)

	head.next = node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5

	Solution().deleteNode(node3)
	while head:
		print(head.val, end="")
		head = head.next

if __name__ == "__main__":
	main()