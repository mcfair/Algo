
class Solution(object):
    def str2tree(self, S):
        """
        :type s: str
        :rtype: TreeNode
        """
        #find the first ')'
        ix = S.find('(')
        
        if ix < 0: #if there is no ')', then its all digits
            return TreeNode(int(S)) if S else None
        
        #find the balanced ')' for the first '('
        bal = 0
        for jx, u in enumerate(S):
            if u == '(': bal += 1
            if u == ')': bal -= 1
            if jx > ix and bal == 0:
                break

        root = TreeNode(int(S[:ix]))
        root.left = self.str2tree(S[ix+1:jx])
        root.right = self.str2tree(S[jx+2:-1])
        return root
