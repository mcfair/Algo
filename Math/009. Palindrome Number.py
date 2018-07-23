#converting num to string is trivial, requires extra space
#find left most and right most number (not character) and compare them
#but how to do it math way? see the smart method below

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x%10==0 and x>0:
            return False
            
        r = 1
        while x / r >= 10:
            r *= 10
        # r is the highest digit of x (10 base)
        # for example,  x=121 -> r = 100

        while r > 1:
        
            #shorten x by triming 1 digit from left
            left, x =divmod(x, r)
            #shorten x by triming 1 digit from right
            x, right = divmod(x, 10)
            
            #compare left & right
            if left != right:
                return False
            #because x has been shorted by 2 digits in each loop
            #so in next loop r = r/100
            r //= 100

        return True
