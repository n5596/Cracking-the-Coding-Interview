# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def recursive(node, k):
            if node.next == None: # reached end
                return 1
            
            val = recursive(node.next, k)
            val += 1
            
            if val == k+1:
                node.next = node.next.next
                return val
            return val
        
        val = recursive(head, n)
        
        if val+1 == n+1: # need to remove head
            head = head.next
        return head
