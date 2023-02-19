# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def recurse(node, p, q):
            if node == None:
                return None, 0
            
            v1, f1 = recurse(node.left, p, q)
            v2, f2 = recurse(node.right, p, q)
            
            if f1 == 2:
                return v1, 2
            if f2 == 2:
                return v2, 2
            
            if (node == p or node == q) and (f1 == 1 or f2 == 1):
                return node, 2
            
            if f1 == 1 and f2 == 1:
                return node, 2
            
            if node == p or node == q:
                return None, f1+f2+1
            
            return None, f1+f2
        
        lca, _ = recurse(root, p, q)
        return lca
