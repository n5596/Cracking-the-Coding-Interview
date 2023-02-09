### Partition list around a pivot: all elements less than pivot are before it, those greater/equal are after it.
import copy

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

def keepingOrder(head, pivot):
	h1 = None
	h2 = None
	h3 = None

	curr = head
	while curr != None:
		if curr.val < pivot:
			if h1 == None:
				h1 = copy.copy(curr)
				e1 = h1
			else:
				e1.next = copy.copy(curr)
				e1 = e1.next
		elif curr.val > pivot:
			if h2 == None:
				h2 = copy.copy(curr)
				e2 = h2
			else:
				e2.next = copy.copy(curr)
				e2 = e2.next
		else:
			if h3 == None:
				h3 = copy.copy(curr)
				e3 = h3
			else:
				e3.next = copy.copy(curr)
				e3 = e3.next
		curr = curr.next

	if h1 == None:
		head = h3
	else:
		head = h1
		e1.next = h3

	e3.next = h2
	if h2 != None:
		e2.next = None
	return head

def notKeepingOrder(head, pivot): 
	curr = head

	h = None
	e = None
	while curr != None:
		if h == None and e == None:
			h = copy.copy(curr)
			e = h	
		elif curr.val < pivot:
			temp = copy.copy(curr)
			temp.next = h
			h = temp
		elif curr.val >= pivot:
			temp = copy.copy(curr)
			e.next = temp
			e = e.next
		curr = curr.next
	e.next = None
	return h

print('Input number of nodes in linked list:')
n = int(input())
print('Input n node values:')
### Construct linked list

elements_in = []
for i in range(n):
	value = int(input())
	if i == 0:
		head = Node(value)
		prev = head
	else:
		curr = Node(value)
		prev.next = copy.copy(curr)
		prev = prev.next
	if value not in elements_in:
		elements_in.append(value)

print('Original linked list:', print_ll(head))
print('Input pivot:')
pivot = int(input())
if pivot not in elements_in:
	print('Pivot not in linked list.')
else:
	print('Keeping order  =========>', print_ll(keepingOrder(head,pivot)))
	print('Not keeping order  =====>', print_ll(notKeepingOrder(head,pivot)))

