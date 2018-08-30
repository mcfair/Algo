class Solution(object):
    def calculate(self, s):
        s = s.strip()+'#' 
        stack = [1]
        lo = 0
        ret = 0
        for hi,c in enumerate(s):
            if not c.isdigit():
                if hi>lo:
                    n = int(s[lo:hi])
                    ret += reduce(operator.mul, stack) * n
                if c == '+':
                    stack[-1] = 1
                elif c == '-':
                    stack[-1] = -1
                elif c == '(':
                    stack.append(1)
                elif c == ')':
                    stack.pop()
                lo = hi+1
            
        return ret
