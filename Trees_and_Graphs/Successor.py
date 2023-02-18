"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here

        def find_in_right_branch(node):
            while node.left != None:
                node = node.left
            return node

        def find_upwards(node, p): # going inorder
            if node == None:
                return None, False

            if node == p: # found it so start looking at parents
                return None, True

            s1, f1 = find_upwards(node.left, p)

            if f1 == True: # found it in left branch
                if s1 != None:
                    return s1, f1
                return node, f1 # current node is successor

            s2, f2 = find_upwards(node.right, p)

            if f2 == True: # found it in right branch
                if s2 != None:
                    return s2, f2
                return None, f2 # cannot find it since  we're in right branch so we go upto parents.
            return None, False

        if root == None or p == None:
            return None

        if p.right != None: # successor will be the leftmost node in the right branch
            return find_in_right_branch(p.right)
        else:
            return find_upwards(root, p)[0]
