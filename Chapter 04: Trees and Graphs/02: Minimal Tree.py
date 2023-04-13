# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def createBST(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            
            mid = (l+r)//2
            
            curr_node = TreeNode(nums[mid])
            curr_node.left = createBST(l,  mid-1)
            curr_node.right = createBST(mid+1, r)
            return curr_node
        
        return createBST(0, len(nums)-1)
