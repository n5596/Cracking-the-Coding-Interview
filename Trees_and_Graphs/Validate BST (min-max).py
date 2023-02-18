# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recurse(node, min_val, max_val):
            if node == None:
                return True
            
            if min_val >= node.val or max_val <= node.val: # invalid condition
                return False
            
            f1 = recurse(node.left, min_val, min(max_val, node.val))
            f2 = recurse(node.right, max(min_val, node.val), max_val)
            
            return f1&f2
        
        return recurse(root, -pow(2,31)-1, pow(2, 31))
