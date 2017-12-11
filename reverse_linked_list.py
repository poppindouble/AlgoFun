class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def reverseList(self, head):
		if not head or not head.next:
			return head
		pre = head
		current = head.next
		pre.next = None

		while current:
			follow = current.next
			current.next = pre
			pre = current
			current = follow
		return pre



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

	newHead = Solution().reverseList(head)
	while newHead:
		print(newHead.val, end="")
		newHead = newHead.next

if __name__ == "__main__":
	main()