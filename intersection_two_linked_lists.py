class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def getIntersectionNode(self, headA, headB):
		lengthA = self.__lengthOfLinkedList__(headA)
		lengthB = self.__lengthOfLinkedList__(headB)

		(longer, shorter) = (headA, headB) if lengthA > lengthB else (headB, headA)
		for _ in range(abs(lengthA - lengthB)):
			longer = longer.next
		while longer:
			if longer == shorter:
				return longer
			longer = longer.next
			shorter = shorter.next


	def __lengthOfLinkedList__(self, head):
		temp = head
		counter = 0
		while temp:
			counter += 1
			temp = temp.next
		return counter
		

def main():
	nodeA1 = ListNode(0)
	nodeA2 = ListNode(1)

	nodeC1 = ListNode(2)
	nodeC2 = ListNode(3)
	nodeC3 = ListNode(4)

	nodeB1 = ListNode(0)
	nodeB2 = ListNode(1)
	nodeB3 = ListNode(3)

	nodeA1.next = nodeA2
	nodeA2.next = nodeC1
	nodeC1.next = nodeC2
	nodeC2.next = nodeC3

	nodeB1.next = nodeB2
	nodeB2.next = nodeB3
	nodeB3.next = nodeC1

	headA = nodeA1
	headB = nodeB1

	print(Solution().getIntersectionNode(headA, headB).val)

if __name__ == "__main__":
	main()