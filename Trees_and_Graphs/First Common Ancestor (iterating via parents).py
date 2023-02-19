# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        parents = {}
        parents[root] = None
        
        def inorder(node):
            if node == None:
                return
            
            if node.left != None:
                parents[node.left] = node
                
            if node.right != None:
                parents[node.right] = node
                
            inorder(node.left)
            inorder(node.right)
            
        inorder(root)
        p_parents = set()
        
        while p != None:
            p_parents.add(p)
            p = parents[p]
            
        if q in p_parents:
            return q
        
        while q != None:
            q = parents[q]
            if q in p_parents:
                return q
