

# O(n) time  44ms
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # O(n) time is esay
        q = collections.deque()
        for x in self.inorder(root):
            if len(q) <k:
                q.append(x.val)
            else:
                if target - q[0] < x.val - target:
                    break
                else:
                    q.popleft()
                    q.append(x.val)
                    
        return list(q)
    
    def inorder (self, root):
        if root:
            for x in self.inorder(root.left): yield x
            yield root
            for x in self.inorder(root.right): yield x
        
