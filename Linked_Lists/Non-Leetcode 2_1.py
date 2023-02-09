### Delete duplicate nodes from linked list
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

def using_hash(head):
	values_in = []
	curr = head
	prev = None
	while curr != None:
		if curr.val in values_in: #duplicate
			curr = curr.next
		else:
			values_in.append(curr.val)
			if prev == None:
				prev = copy.copy(curr)
			else:
				prev.next = curr
				prev = prev.next
			curr = curr.next
	prev.next = None
	return head

def brute_force(head):
	c1 = head
	while c1 != None:
		c2 = copy.copy(c1)
		while c2 != None and c2.next != None:
			if c1.val == c2.val: #duplicate
				c2.next = c2.next.next
			c2 = c2.next
		c1 = c1.next
	return head

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


print('Original linked list:', print_ll(head))
print('Hash table method: O(n) time and O(n) space ======>', print_ll(using_hash(head)))
print('Brute force: O(n^2) time and O(1) space ==========>', print_ll(brute_force(head)))
