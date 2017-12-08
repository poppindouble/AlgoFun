"""
make two pointer, turtle and rabbit
Turtle is runing 1 step at a time
Rabbit is running 2 steps at a time
let's assume when Turtle enter the circle, the Rabbit is N steps ahead Turtle
and the circle length is L
first, let's assume Turtle and Rabbit will meet at point M,
so, let's say if the Turtle runs for a full circle L, turtle went back to the origin of the circle
the rabbit already run 2 full circle, which is 2L
consider when rabbit run (L/2), which is on the opposite side of the origin of the circle, but Rabbit alreay finish a full L
Anyways, before Turtle finish a full circle, rabbit will meet turtle

So, which we can also think, it is actually rabbit is L - N behind the turtle, then the Rabbit start to chasing the Turtle
when they meet at M, let's say Turtle runs S
so rabbit actually runs (L - N) + S
so 
2 * t = (L - N) + S
1 * t =  S

=> S = L - N
So, they actually met N steps before the origin

"""

class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution():
	def hasCycle(self, head):
		if not head:
			return False

		turtle = head
		rabbit = head

		while rabbit.next and rabbit.next.next:
			rabbit = rabbit.next.next
			turtle = turtle.next
			if rabbit == turtle:
				return True

		return False


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
	node5.next = node3

	print(Solution().hasCycle(head))

if __name__ == "__main__":
	main()