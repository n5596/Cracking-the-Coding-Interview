# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = collections.deque([(root, 0)])
        
        levels = []
        curr_level = []
        
        while len(queue) > 0:
            node, lvl = queue.popleft()
            curr_level.append(node.val)
            
            if node.left != None:
                queue.append((node.left, lvl+1))
            if node.right != None:
                queue.append((node.right, lvl+1))
                
            if len(queue) == 0 or lvl != queue[0][1]: # new level
                levels.append(curr_level)
                curr_level = []
                
        return levels
