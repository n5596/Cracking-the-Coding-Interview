### Return kth to last node

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

def print_node(node):
	if node == None:
		u = None
	else:
		u = node.val
	return u

def length_known(head, n, k):
	count = 0
	curr = head
	while curr != None:
		count += 1
		if count == n-k+1:
			return curr
		curr = curr.next
	return curr

def recursive(head, k):
	if head == None:
		return 0, None
	
	next_node, ptr = recursive(head.next, k)
	if next_node+1 == k: #this is the node
		return -1, head
	if ptr != None:
		return -1, ptr
	return next_node+1, None

def iterative(head, k):
	ahead = 0
	fast = head
	slow = head
	while fast != None and ahead < k:
		ahead += 1
		fast = fast.next	
	
	steps = 0
	while fast != None:
		fast = fast.next
		slow = slow.next	
	return slow

print('Input number of nodes in linked list:')
n = int(input())
print('Input n node values:')
### Construct linked list
for i in range(n):
	value = int(input())
	if i == 0:
		head = Node(value)
		prev = head
	else:
		curr = Node(value)
		prev.next = copy.copy(curr)
		prev = prev.next
print('Input k (should not be more than n)')
k = int(input())
if k > n:
	print('Testcase will not work')
else:
	print('Original linked list:', print_ll(head))
	print('Length is known: O(n) time =====>', print_node(length_known(head, n, k)))
	print('Length unknown: Recursive ======>', print_node(recursive(head, k)[1]))
	print('Length unknown: Iterative ======>', print_node(iterative(head, k)))
