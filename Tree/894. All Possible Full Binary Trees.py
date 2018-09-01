class Solution(object):
    def __init__(self):
        self.memo = {}
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N%2==0: return []
        if N==1: return [TreeNode(0)]
        if N in self.memo: return self.memo[N]
        
        ans = []
        for i in range(1, N, 2):
            for l in self.allPossibleFBT(i):
                for r in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = l 
                    root.right = r
                    ans.append(root)
        self.memo[N] = ans
        return ans
