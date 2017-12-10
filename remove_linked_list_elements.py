"""
the first solution is hard to code
so always think about adding a dummy head when we deal with linked list
"""

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	# def removeElements(self, head, val):
	# 	if not head:
	# 		return head
	# 	while head.val == val:
	# 		temp = head.next
	# 		head.next = None
	# 		head = temp
	# 		if not head:
	# 			return head

	# 	detector = head.next
	# 	temp = head

	# 	while detector:
	# 		if detector.val == val:
	# 			while temp.next != detector:
	# 				temp = temp.next
	# 			temp.next = detector.next
	# 			detector.next = None
	# 			detector = temp.next
	# 			continue
	# 		detector = detector.next

	# 	return head

	def removeElements(self, head, val):
		dummyHead = ListNode(val + 1)
		dummyHead.next = head

		temp = dummyHead
		detector = head

		while detector:
			if detector.val == val:
				while temp.next != detector:
					temp = temp.next
				temp.next = detector.next
				detector.next = None
				detector = temp.next
				continue
			detector = detector.next
		return dummyHead.next

def main():
	head = ListNode(1)
	node1 = ListNode(6)
	node2 = ListNode(6)
	node3 = ListNode(4)
	node4 = ListNode(5)
	node5 = ListNode(6)
	node6 = ListNode(6)
	node7 = ListNode(0)


	head.next = node1
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node5.next = node6
	node6.next = node7

	newHead = Solution().removeElements(head, 6)
	temp = newHead

	while temp:
		print(temp.val, end=' ')
		temp = temp.next

if __name__ == "__main__":
	main()