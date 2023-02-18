# Inorder approach but without using extra space. We just keep track of previous node instead of all nodes in inorder order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(node, prev_node):
            
            flag =  True
            next_node = node
            
            if node.left != None:
                flag, prev_node = inorder(node.left, prev_node)
            
            # check if largest node in left branch is smaller than current node
            if flag == False or  (prev_node != None and prev_node.val >= node.val):
                return False, node
            
            if node.right != None:
                if node.val >= node.right.val: # check if current node is less than the right node
                    return False, node
                flag, next_node = inorder(node.right, node)
                
            return flag, next_node
        
        flag, _ = inorder(root, None)
        return flag
