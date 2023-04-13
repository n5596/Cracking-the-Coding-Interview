#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list

        count = {}
        
        curr = head
        prev = None
        
        while curr != None:
            if curr.data not in count:
                count[curr.data] = 1
                prev = curr
            else:
                prev.next = curr.next # skip
                
            curr = curr.next
        return head
