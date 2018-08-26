#another DFS  
class Solution(object):
    def pathSum(self, root, sumv):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        
        ans = []
        def dfs(node, v, path):
            if not node.left and not node.right and v==sumv:
                ans.append(path)
                return 
            if node.left:
                dfs(node.left, v+node.left.val, path+[node.left.val])
            if node.right:
                dfs(node.right, v+node.right.val, path+[node.right.val])
        dfs(root, root.val, [root.val])  
        return ans
            
#another BFS
class Solution(object):
    def pathSum(self, root, sumv):

        if not root: return []
        ret = []
        q = collections.deque([(root, sumv-root.val, [root.val])])
        while q:
            node, sums, path = q.popleft()  
            if not node.left and not node.right and sums==0:
                ret.append(path)
            if node.left:
                q.append([node.left, sums-node.left.val, path+[node.left.val] ])
            if node.right:
                q.append([node.right, sums-node.right.val, path+[node.right.val] ])
        
        return ret
                
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
