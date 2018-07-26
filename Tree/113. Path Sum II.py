#DFS
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
    
             dfs(root.left, sum-root.val, path+[root.val] )
        
             dfs(root.right, sum-root.val, path+[root.val] )
         
          
        dfs(root, sum, [])
        return ret
#BFS

def pathSum(self, root, sum):
    res = []
    queue =  collections.deque([(root, sum, [])])
    while queue:
        node, sum, path = queue.popleft()
        if node:
            if node.val == sum and not node.left and not node.right:
                res.append(path+[node.val])
                continue
            queue.append((node.left, sum-node.val, path+[node.val]))
            queue.append((node.right, sum-node.val, path+[node.val]))
    return res
