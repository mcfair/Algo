"""
There is one imporant observation we can make about the number of bits in each number.

Each Power of 2 has exactly only 1 bit. (2 : 0010 , 4: 0100, 8:1000, 16:10000)
Each number after the power of 2 follows a pecular pattern :
0 → 0
1 → 1
2 → 1 + dp[0] Nearest Power of 2
3 → 1 + dp[1] 1 greater than nearest
4 → 1 + dp[0] Nearest
5 → 1+ dp[1] 1 greater than nearest
6 → 1+ dp[2] 2 greater than nearest
7 → 1+ dp[3] 3 greater than nearest
8 → 1+ dp[0] Nearest
9 → 1+ dp[1]
10 → 1+ dp[2]
11 → 1+ dp[3]
12 → 1+ dp[4]
"""

def countBits(self, num):
    def isPowerOf2(x):
        return x&(x-1)==0
    
    dp = [0] + [1]*num
    i = 2
    prev_powerOf2 = 0
    
    while i <= num:
        if isPowerOf2(i):
            prev_powerOf2 = i
            dp[i] = 1
        else:
            dp[i] = 1 + dp[i - prev_powerOf2]
         i+=1
    return dp
    
 """
 Another way of dynamic programming, considering binary representation
 dp[i] = dp[i>>1] + i&1
 current counts = counts of right shift(subproblem)  +  current bit
 """
 def countBits(self, num):
     dp = [0]*(num+1)
     for i in range(1,num+1):
        dp[i] = dp[i>>1] + (i&1)
     return dp
