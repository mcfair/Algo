#Top down, DFS + Memo
def getMoneyAmount(self, n):
    memo = {}
    def dfs(lo, hi):
        if lo>=hi: 
            return 0
        if (lo,hi) in memo:
            return memo[lo,hi]

        res = float('inf')
        #take "i" that cost the least
        #for each choice of i, the cost = max(dfs(lo,i-1)+i, dfs(i+1, hi)+i)
        for i in range(lo,hi):
            res = min(res, i + max(dfs(lo,i-1), dfs(i+1, hi)))
            
        memo[lo,hi] = res
        return res

    return dfs(1,n)
  
"""
Let's take an instance, for n = 3, we have 3 choices either to choose 1 or 2 or 3.
Let's say we choose 1. There are 2 possible chances,

[Case X]: 1 is the actual number so you pay 0$ or,
[Case Y]: 1 is not the actual number so you pay 1$ (now you know that the actual number is > 1 because for every guess we will know if its less than or greater than, in our case it can only be greater than) and have the subproblem (2, 3). To choose from (2, 3) again recursively applying the same method, you can choose either 2 or 3. If you pick 2, you have 2 possible outcomes again. 2 is the actual number and you pay 0$ for this choice or 2 is not the actual number and you pay 2$ for this choice and you know 3 is the answer since that's the only one left. On the other hand, if you had picked 3, then either 3 is correct or you pay 3$ and know 2 is the actual answer since it's the only one left. So to sum up this, you pay 2$ in the worst case if you choose 2 or pay 3$ in the worst case if you pick 3$. So we will pick the min of the worst cases which is 2$ and hence 2 is the answer for (2, 3) subproblem. (Notice the minimax? ;) ) So, the total cost paid in this is 1$ + 2$ = 3$.
Let's say you picked 2 initially. You have 2 possible outcomes.

2 is the actual number and you pay 0$ or,
2 is not the actual number and you pay 2$. At this point, you get to know if the actual number is less than or greater than the actual number. So, you will know the answer right away without another guess. So you end up paying 2$.
So, if you choose 2 initially, you risk paying 2$ at most.
Similarly, if you had chosen 3 initially, you risk paying 4$ at most. Hence picking 2 initially is the best option and you risk at most 2$.
This leads to a natural recursion, which you can find in the code below. I have memoized it in a matrix.
"""
