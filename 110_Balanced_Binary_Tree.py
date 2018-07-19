# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#!!! DFS function can return any number of variables for your need.

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        Use dfs function "check" to return two things :
        (1)tree_height and (2)whether subtree is balanced
        """
         
        def check(node):
            #return (tree_height, balanced_boolean)
            if not node: return (0, True)
            
            lh, lb = check(node.left)
            rh, rb = check(node.right)
            balanced = lb and rb and abs(lh-rh)<=1
            return (1+max(lh,rh),  balanced)
        
        return check(root)[1]
