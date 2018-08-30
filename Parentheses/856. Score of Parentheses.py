 
class Solution:
    def scoreOfParentheses(self, S):
        stack, res = [], 0
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                last = stack.pop()
                add =  2 * last or 1
                if stack:
                    stack[-1] += add
                else:
                    res += add
        return res


#Smart cheat!
def scoreOfParentheses(self, S):
        return eval(S.replace(')(', ')+(').replace('()', '1').replace(')', ')*2'))
