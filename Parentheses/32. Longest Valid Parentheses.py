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

    
  
#less readability, but faster
#use stack to store the value of "i-stack[-1]" in the method above
class Solution:
    def longestValidParentheses(self, s):
        
        stack = [0]
        longest = 0
        
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest
