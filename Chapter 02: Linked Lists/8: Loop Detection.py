# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        slow, fast = head, head
        flag = 0
                
        while flag == 0 or slow != fast:
            slow = slow.next
            
            if fast == None or fast.next == None:
                return None
            fast = fast.next.next
            flag = 1
            
            
        collision_point = fast
        slow = head
        
        # both collision point and head are equidistant from the start of the loop
        while slow != fast:
            slow = slow.next
            fast = fast.next
            
        return slow
