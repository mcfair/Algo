"""
    logic is for each path keep a count
    update a global maxlen
"""
class Solution(object):
    def longestUnivaluePath(self, root):

        if not root: return 0
        
        def dfs(root ):
            l,r=0,0
            if root.left:
                l=dfs(root.left )
                l=l+1 if root.left.val==root.val else 0
            if root.right:
                r=dfs(root.right )
                r=r+1 if root.right.val==root.val else 0
                
            self.ans = max(self.ans,r+l)
            return max(l,r)
        
        self.ans = 0
        dfs(root)
        return self.ans
