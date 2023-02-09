### Design a stack in which push, pop and min operate in O(1) time
class Stack:
	def __init__(self):
		self.stack = []
		self.minimums = []
		self.top = 0

	def push(self, value):
		self.stack.append(value)
		if self.minimums == [] or (len(self.minimums)>0 and value <= self.minimums[-1]):
			self.minimums.append(value)
		self.top += 1

	def pop(self):
		if self.top == 0: 
			print('Empty stack. Not possible to pop')
		else:
			if self.stack[-1] == self.minimums[-1]:
				self.stack.pop()
				self.minimums.pop()
			else:
				self.stack.pop()
			print('Stack is:', self.print_stack())
			self.top -= 1
	
	def min(self):
		if self.top == 0:
			print('Empty stack. No minimum')
		else:
			print('Minimum is:',self.minimums[-1])

	def print_stack(self):
		return self.stack


print('Input number of operations:')
n = int(input())
s = Stack()

print('Input operations:') #Operations of type FindMin, Pop, Pushx where x is an integer 
for i in range(n):
	op = input()
	if op == 'FindMin':
		s.min()
	elif op[0:3] == 'Pop':
		s.pop()
	else:
		push_val = int(op[4:])
		s.push(push_val)
		print('Stack is:', s.print_stack())

