### Check to see if two lists intersect

import copy
import random

class Node:
	def __init__(self, value):
		self.val = value
		self.next = None

def print_ll(head):
	ll_values = []
	curr = head
	while curr != None:
		ll_values.append(curr.val)
		curr = curr.next

	return ll_values

def detect_intersection(head1, head2):
	c1 = head1
	c2 = head2
	count1 = 1
	count2 = 1

	while c1.next != None:
		c1 = c1.next
		count1 += 1
	while c2.next != None:
		c2 = c2.next
		count2 += 1

	if c1 != c2:
		print('Found no intersection')
		return

	if count2 < count1:
		a1 = head1
		advance = 0
		while advance < abs(count1-count2):
			advance += 1
			a1 = a1.next
		c2 = head2
		while a1 != c2 and c2 != None:
			a1 = a1.next
			c2 = c2.next
		print('Found intersection at:', a1, ' with value:', a1.val)
	else:
		a2 = head2
		advance = 0
		while advance < abs(count1-count2):
			advance += 1
			a2 = a2.next
		c1 = head1
		while a2 != c1 and c1 != None:
			a2 = a2.next
			c1 = c1.next
		print('Found intersection at:', a2, ' with value:', a2.val)
	return

n1 = random.randint(10,100)
n2 = random.randint(10,100)

for i in range(n1):
	value = random.randint(1,1000)
	if i == 0:
		head1 = Node(value)
		prev1 = head1
	else:
		curr = Node(value)
		prev1.next = copy.copy(curr)
		prev1 = prev1.next
prev1.next = None

for i in range(n2):
	value = random.randint(1,1000)
	if i == 0:
		head2 = Node(value)
		prev2 = head2
	else:
		curr = Node(value)
		prev2.next = copy.copy(curr)
		prev2 = prev2.next
prev2.next = None

loop = random.random()
if loop < 0.3: #no intersection
	print('No Intersection')
else:	
	which_list = random.random()
	if which_list < 0.5: #attach l2 to l1
		attach_node = random.randint(2,n1)
		count = 0
		curr = head1
		while curr != None:
			count += 1
			if count == attach_node:
				prev2.next = curr
				break			
			curr = curr.next
	else:
		attach_node = random.randint(2,n2)
		count = 0
		curr = head2
		while curr != None:
			count += 1
			if count == attach_node:
				prev1.next = curr
				break
			curr = curr.next

	print('Intersection at:', curr,' with value:', curr.val)

detect_intersection(head1, head2)
