class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ret = []
        def dfs(root, sum, path):
            if not root:
                return
            if not root.left and not root.right and sum==root.val:
                ret.append(path+[root.val])
                return 
            
            if root.left:
                dfs(root.left, sum-root.val, path+[root.val] )
            if root.right:
                dfs(root.right, sum-root.val, path+[root.val] )
         
          
        dfs(root, sum, [])
        return ret
