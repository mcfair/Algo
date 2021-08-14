"""
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The longest consecutive path needs to be from parent to child (cannot be the reverse).
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def search(node, patval, track):
            if not node:
                self.ans = max(self.ans, track)
                return None
            if node.val == patval+1:
                search(node.left, node.val, track+1)
                search(node.right, node.val, track+1)
            elif node.val != patval+1:
                self.ans = max(self.ans, track)
                search(node.left, node.val, 1)
                search(node.right, node.val, 1)                
        self.ans = 1    
        search(root,float('inf'),1)        
            
        return self.ans
