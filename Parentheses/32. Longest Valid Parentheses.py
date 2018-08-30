class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        ans = 0
        for i, c in enumerate(s):
            if len(stack)>1 and s[stack[-1]]=='(' and c==')':
                stack.pop()
                ans = max(ans, i-stack[-1])
            else:
                stack.append(i)
         
        return ans
