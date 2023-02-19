# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def matchTree(node1, node2):
            if node1 == None and node2 == None:
                return True
            
            if node1 == None or node2 == None:
                return False
            
            if node1.val != node2.val:
                return False
            
            f1 = matchTree(node1.left, node2.left)
            f2 = matchTree(node1.right, node2.right)
            
            return f1 & f2
        
        def iterate(node, subroot):
            if node == None:
                return False
            
            if node.val == subroot.val:
                boolean = matchTree(node, subroot)
                    
                if boolean:
                    return True
                
            f1 = iterate(node.left, subroot)
            f2 = iterate(node.right, subroot)
            return f1 | f2
        
        return iterate(root, subRoot)
