class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        for i, c in enumerate(s):
            if stack and s[stack[-1]]=='(' and c==')':
                stack.pop()
            else:
                stack.append(i)
                
        #indices left inside stack are not paired
        #find the max distance between indices
        stack = [-1]+stack+[len(s)] 
        ans = 0
        for i in range(1, len(stack)):
            ans = max(ans, stack[i]-stack[i-1]-1)
        return ans
