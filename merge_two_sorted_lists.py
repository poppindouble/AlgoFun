class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# oops, I thougt it was normal list, but the question is actually listnode
	# def mergeTwoLists(self, l1, l2):
	# 	result = []
	# 	m, n = 0, 0
	# 	if not l1:
	# 		return l2
	# 	if not l2:
	# 		return l1
	# 	for _ in range(len(l1) + len(l2)):
	# 		if l1[m] > l2[n]:
	# 			result.append(l2[n])
	# 			n += 1
	# 		else:
	# 			result.append(l1[m])
	# 			m += 1

	# 		if m == len(l1):
	# 			return result + l2[n:]
	# 		if n == len(l2):
	# 			return result + l1[m:]
	# 	return result


	def mergeTwoLists(self, l1, l2):
		pointer1 = l1
		pointer2 = l2
		result = ListNode(100)
		temp = result

		while pointer1 and pointer2:
			if pointer1.val < pointer2.val:
				temp.next = pointer1
				pointer1 = pointer1.next
			else:
				temp.next = pointer2
				pointer2 = pointer2.next
			temp = temp.next

		if not pointer1:
			temp.next = pointer2
		if not pointer2:
			temp.next = pointer1

		return result.next


def main():
	node1 = ListNode(1)
	node2 = ListNode(2)
	node6 = ListNode(6)
	node9 = ListNode(9)
	node17 = ListNode(17)
	node20 = ListNode(20)
	node34 = ListNode(34)

	# l1: node1 -> node9 -> node 17
	# l2: node2 -> node6 -> node20 -> node34
	node1.next = node9
	node9.next = node17
	l1 = node1

	node2.next = node6
	node6.next = node20
	node20.next = node34
	l2 = node2

	result = Solution().mergeTwoLists(None, l2)

	while result:
		print(result.val)
		result = result.next

if __name__ == "__main__":
	main()