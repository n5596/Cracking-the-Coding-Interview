### Loop detection

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

def loop_detect(head):
	fast = head
	slow = head
	flag = 0

	while flag == 0 or (fast != None and fast != slow and fast.next != None):
		fast = fast.next.next
		slow = slow.next
		flag = 1

	if fast == None or fast.next == None:
		if fast != None:
			print(fast.val, fast, fast.next)
		print('Found no Loop')
		return

	slow = head
	while fast != slow:
		fast = fast.next
		slow = slow.next
	
	print('Found loop at:', fast,' with value:', fast.val)
	return 

n = random.randint(10,100)
loop_at = random.randint(1,n)

store_loop = None
for i in range(n):
	value = random.randint(1,1000)
	if i == 0:
		head = Node(value)
		prev = head
	else:
		curr = Node(value)
		prev.next = copy.copy(curr)
		prev = prev.next

#print('Linked List (without loop)', print_ll(head), prev.val, prev)
loop = random.random()
if loop < 0.1: #no loop
	prev.next = None
	print('No Loop')
else:	
	count = 0
	curr = head
	while curr != 0:
		count += 1
		if loop_at == count:
			prev.next = curr
			break
		curr = curr.next
	print('Loop at:', curr,' with value:', curr.val)

loop_detect(head)

