"""
Use the turtle rabbit thinking again
when turtle went to the end,
turtle suppose to be in the middle of a linked list

we can use stack to keep previous value
or we can reverse the rest of the linked list and compare again
"""

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	# def isPalindrome(self, head):
	# 	if not head: return head
	# 	rabbit = head
	# 	turtle = head
	# 	myStack = []
	# 	while rabbit and rabbit.next:
	# 		myStack.append(turtle)
	# 		turtle = turtle.next
	# 		rabbit = rabbit.next.next
	# 	if rabbit: turtle = turtle.next
	# 	while myStack:
	# 		current = myStack.pop()
	# 		if current.val != turtle.val:
	# 			return False
	# 		turtle = turtle.next
	# 	return True

	def isPalindrome(self, head):
		if not head: return head
		rabbit = head
		turtle = head

		while rabbit.next and rabbit.next.next:
			turtle = turtle.next
			rabbit = rabbit.next.next

		newHead = self.__reverseLinkedList__(turtle.next)
		# first half of linked list might be have one element more then
		# the second half
		while newHead:
			if head.val != newHead.val:
				return False
			newHead = newHead.next
			head = head.next
		return True


	# pay attention to this way to reverse a linked list
	def __reverseLinkedList__(self, head):
		if (not head) or (not head.next): return head
		temp = head
		head = self.__reverseLinkedList__(head.next)
		temp.next.next = temp
		temp.next = None
		return head


def main():
	head = ListNode(0)
	node1 = ListNode(1)
	node2 = ListNode(2)
	nodeMid = ListNode(100)
	node3 = ListNode(2)
	node4 = ListNode(1)
	node5 = ListNode(0)


	head.next = node1
	node1.next = node2
	node2.next = nodeMid
	nodeMid.next = node3
	# node2.next = node3
	node3.next = node4
	node4.next = node5

	print(Solution().isPalindrome(head))

if __name__ == "__main__":
	main()