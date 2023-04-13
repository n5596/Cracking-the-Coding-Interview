# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        before, after = None, None
        before_head, after_head = None, None
        
        curr = head
        
        while curr != None:
            if curr.val < x:
                if before == None:
                    before = ListNode(curr.val)
                    before_head = before
                else:
                    before.next = ListNode(curr.val)
                    before = before.next
            else:
                if after == None:
                    after = ListNode(curr.val)
                    after_head = after
                else:
                    after.next = ListNode(curr.val)
                    after = after.next
            curr = curr.next
            
        if before_head == None:
            return after_head
        
        before.next = after_head
        return before_head
