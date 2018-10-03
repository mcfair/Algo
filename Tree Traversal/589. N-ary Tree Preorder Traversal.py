#Recursive solution is trivial
class RecursiveSolution(object):
    def preorder(self, root):
        if not root: 
            return []
        t=[root.val]
        for i in root.children:
            t+=self.preorder(i)
        return t
        
 #Iterative Solution
 class IterativeSolution(object):
    def preorder(self, root):
        stack = [root]
        res = []
        while stack:
            p=stack.pop()
            if p:
                res.append(p.val)
                for i in reversed(range(len(p.children))): 
                    stack.append(p.children[i])
        return res
