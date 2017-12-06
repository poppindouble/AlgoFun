class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self, head):
		if head is None:
			return None

		i = j = head
		while j is not None:
			if j.val == i.val:
				j = j.next
				continue
			i.next = j
			i = j
		i.next = None
		return head

def main():
	head = ListNode(1)
	node1 = ListNode(1)
	node2 = ListNode(2)
	node3 = ListNode(3)
	node4 = ListNode(3)
	node5 = ListNode(3)
	node6 = ListNode(3)

	head.next = node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6

	head = Solution().deleteDuplicates(head)

	i = head
	while i is not None:
		print(i.val)
		i = i.next

if __name__ == "__main__":
	main()