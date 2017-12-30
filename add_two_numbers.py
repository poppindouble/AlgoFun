class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	# def addTwoNumbers(self, l1, l2):
	# 	result = self.__getRealNumber__(l1) + self.__getRealNumber__(l2)
	# 	head = ListNode(-1)
	# 	temp = head
	# 	while result:
	# 		lastDigit = result % 10
	# 		result //= 10
	# 		temp.next = ListNode(lastDigit)
	# 		temp = temp.next
	# 	return head.next


	# def __getRealNumber__(self, head):
	# 	result = 0
	# 	temp = head
	# 	digit = 1
	# 	while temp:
	# 		result += temp.val * digit
	# 		digit *= 10
	# 		temp = temp.next
	# 	return result

	def addTwoNumbers(self, l1, l2):
		head = ListNode(0)
		curr = head
		carry = 0
		while l1 or l2:
			num1 = 0 if not l1 else l1.val
			num2 = 0 if not l2 else l2.val
			temp = num1 + num2 + carry
			curr.next = ListNode(temp % 10)
			carry = temp // 10
			curr = curr.next
			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next
		if carry:
			curr.next = ListNode(1)
		return head.next

def main():
	l1 = ListNode(2)
	node1 = ListNode(4)
	node2 = ListNode(3)
	l1.next = node1
	node1.next = node2

	l2 = ListNode(5)
	node4 = ListNode(6)
	node5 = ListNode(4)
	l2.next = node4
	node4.next = node5

	head = Solution().addTwoNumbers(l1, l2)
	while head:
		print(head.val, end=" ")
		head = head.next

if __name__ == "__main__":
	main()