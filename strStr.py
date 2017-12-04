"""
To solve this question, we need KMP algorithm
Here is a pretty good resource to understand how KMP algorithm works
https://www.youtube.com/watch?v=GTJr8OvyEVQ

let's say our pattern is needle = aabaabaaa
the string we need to search is hayStack = aabaac + aaa + aabaabaay + aabaabaaa

so the needle does match at the last part of the hayStack

let's have a look at first part
define a pointer j, which is sliding on p
define a pointer i, which is sliding on hayStack
both started at 0.
everytime these is a match, both move on
hayStack = aabaac
p        = aabaabaaa

it stops matching at j = 5, i = 5, hayStack[5] = c but p[5] = b
what we don't want to do is that we start to compare like this:
hayStack = aabaac
p        =  aabaabaaa

in this way the complexity will be O(m * n)

what we want is this
hayStack = aabaac
p        =    aabaabaaa

because we know when the fail happen at p[5], the two characters in front of it is aa, which also matches hayStack[3~4]
which also matches p[0~1]

so what we want is 
once a fail happen, keep i at the same position, because we are not sure the current hayStack[i] will be part of the final answer
move our j to 2, then we will get to the point above

let's see two more example:

1.

hayStack[6~8] = aaa
p             = aabaabaaa

fail at j = 2, hayStack[8] = a, p[2] = b
what we want is this:

hayStack[6~8] = aaa
p             =  aabaabaaa
---------------------------


2.

hayStack[9~17] = aabaabaay
p              = aabaabaaa

fail at j = 8, hayStack[17] = y, p[8] = a
what we want is this:

hayStack[9~17] = aabaabaay
p              =    aabaabaaa

--------------------------------------------------------------

from above we can see, we need a table to tell pointer j where to move to when failure happen, that's KMP algo

let's keep our pattern, and let's say this is our table:

j         0 1 2 3 4 5 6 7 8
p       = a a b a a b a a a
next[j] = 0 1 0 1 2 3 4 5 2

==========================
hayStack = aabaac
p        = aabaabaaa

fail at j = 5, we move to next[5 - 1] = 2

hayStack = aabaac
p        =    aabaabaaa
==========================

==========================
hayStack[6~8] = aaa
p             = aabaabaaa

fail at j = 2, we move to next[2 - 1] = 1

hayStack[6~8] = aaa
p             =  aabaabaaa
==========================

==========================
hayStack[9~17] = aabaabaay
p              = aabaabaaa

fail at j = 8, we move to next[8 - 1] = 5

hayStack[9~17] = aabaabaay
p              =    aabaabaaa
==========================

And yes, you can tell from above, the last element in next[j] will never getting accessed.......
in our example, which is next[8]

OK, then our first task is to construct this table
j         0 1 2 3 4 5 6 7 8
p       = a a b a a b a a a
next[j] = 0 1 0 1 2 3 4 5 2

next[0] always gonna be 0
next[j] is the lenth of longest proper prefix which is also a proper surfix in substring p[0 ~ j]
it sounds horrible, let me translate it into English.

************
next[0] = 0
************
next[1]:
subString p[0 ~ j] = p[0 ~ 1] = aa
longest proper prefix: a
longest proper surfix: a
length of it = 1
next[1] = 1
************
next[2]:
subString p[0 ~ j] = p[0 ~ 2] = aab
longest proper prefix: ''
longest proper surfix: ''
length of it = 0
next[2] = 0
************
next[3]:
subString p[0 ~ j] = p[0 ~ 3] = aaba
longest proper prefix: a
longest proper surfix: a
length of it = 1
next[3] = 1
************
next[4]:
subString p[0 ~ j] = p[0 ~ 4] = aabaa
longest proper prefix: aa
longest proper surfix: aa
length of it = 2
next[4] = 2
************
next[5]:
subString p[0 ~ j] = p[0 ~ 5] = aabaab
longest proper prefix: aab
longest proper surfix: aab
length of it = 3
next[5] = 3
************
next[6]:
subString p[0 ~ j] = p[0 ~ 6] = aabaaba
longest proper prefix: aaba
longest proper surfix: aaba
length of it = 4
next[6] = 4
************
next[7]:
subString p[0 ~ j] = p[0 ~ 7] = aabaabaa
longest proper prefix: aabaa
longest proper surfix: aabaa
length of it = 5
next[7] = 5
************
well, this one will never be used...
next[8]:
subString p[0 ~ j] = p[0 ~ 8] = aabaabaaa
longest proper prefix: aa
longest proper surfix: aa
length of it = 2
next[8] = 2
************

here is how we gonna code it:
make two pointer again, i and j
i start from 1, i is the pointer pointing to the current one we need to fill in the next function
j start from 0, which represent the index of last element of the longest prefix

i         0 1 2 3 4 5 6 7 8
j         0 1 2 3 4 5 6 7 8
p       = a a b a a b a a a
next[j] = 0 1 0 1 2 3 4 5 2


let's started:
--------------------
i = 1, j = 0
p[i] = p[1] = a
p[j] = p[0] = a
p[i] == p[j]
next[i] = j + 1 = 0 + 1 = 1
i forward
j forward
--------------------
i = 2, j = 1
p[i] = p[2] = b
p[j] = p[1] = a
p[i] != p[j]

at any time, when p[i] != p[j], which means, you can not include p[i] as part of the longest prefix/surfix.
which also means p[0 ~ j-1] == p[i - next[i - 1], i - 1], So, the thinking here becomes intersting:

1. next[i - 1] represent the length of longest prefix/surfix which include p[i - 1] as well, next[i - 1] = j, but p[j] != p[i]

j = next[i - 1]

2. next[next[i - 1] - 1] which is also next[j - 1] represent the length of longest prefix/surfix which include p[j - 1] as well, 
so, maybe, if we compare with p[next[j - 1]] with p[i] might worked out, because, p[next[j - 1]] is actually the next character of the
longest prefix which include p[j -1] as well, if they are ==, then you find the length of longest prefix/surfix for i th position,
which is next[j - 1] + 1, otherwise keep recursing.

j = next[j - 1]

then it is gonna be keep finding 

it is like at position i, it is trying to hold as many possible numbers for the longest surfix

so:
j = next[j - 1] = next[0] = 0
p[i] != p[0], so next[i] = 0
i forward
j stay
--------------------

i = 3, j = 0
p[i] = p[3] = a
p[j] = p[0] = a
p[i] == p[j]
i forward
j forward
--------------------

it will keep going until
i = 8, j = 5
p[i] = p[8] = a
p[j] = p[5] = b
p[i] != p[j]

j = next[j - 1] = next[4] = 2
p[2] = b
p[2] != p[i]

j = next[j - 1] = next[1] = 1
p[1] = a
p[j] == p [i]
p[i] = j + 1 = 2
i forward
j forward
--------------------

"""


class Solution:
	def strStr(self, hayStack, needle):

		if needle == "":
			return 0

		next = self.__generateFaultArray__(needle)

		i, j = 0, 0
		while i < len(hayStack):
			if hayStack[i] == needle[j]:
				i += 1
				j += 1
				if j == len(needle):
					return i - len(needle)
			else:
				if j == 0:
					i += 1
				else:
					j = next[j - 1]

		return -1

	def __generateFaultArray__(self, needle):
		i, j = 1, 0
		next = [0] * len(needle)

		while i < len(needle):
			if needle[i] == needle[j]:
				next[i] = j + 1
				i += 1
				j += 1
			else:
				if j == 0:
					next[i] = 0
					i += 1
				else:
					j = next[j - 1]

		return next

def main():
	print(Solution().strStr("", ""))

if __name__ == "__main__":
	main()