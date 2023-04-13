# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next == None:
            return True
        
        slow, fast = head, head
        stack = []
        odd_flag = False
        
        # slow will hit midpoint
        while fast != None and fast.next != None:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
            
            if fast != None and fast.next == None:
                odd_flag = True

        
        if odd_flag: # skip the middle node in odd list
            slow = slow.next
            
        while slow != None:
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True
