# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root == None:
            return True
        
        def recurse(node, height):
            if node == None:
                return True, height
            
            f1, h1 = recurse(node.left, height+1)
            f2, h2 = recurse(node.right, height+1)
            
            if f1 == False or f2 == False or abs(h1-h2) > 1:
                return False, max(h1, h2)
            
            return True, max(h1, h2)
        
        flag, _ = recurse(root, 0)
        return flag
