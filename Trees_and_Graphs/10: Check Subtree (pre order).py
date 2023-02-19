# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preorder_string(node, s):
            if node == None:
                s += '*'
                return s
            
            s += "-"+str(node.val)+"-"
            s = preorder_string(node.left, s)
            s = preorder_string(node.right, s)
            return s
        
        s1 = preorder_string(root, "")
        s2 = preorder_string(subRoot, "")

        if s2 in s1:
            return True
        return False
