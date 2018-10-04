"""
Three Methods:
DFS + Memo --> easy to write in interview and error-proof
Single DP from bottom-right corner to top-left corner --> clean code if edge cases handled properly
Double DP, maintain two matrix: minInitHP, currHP --> difficult to get minmax correct, error-prone
"""
class DFS_Solution(object):
    def calculateMinimumHP(self, dungeon):

        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n: 
                return float('inf')
            if (i,j) in memo:
                return memo[i,j]
            if (i,j) == (m-1,n-1):
                health = 1        #success condition: health=1 at bottom-right corner
            else:
                health = min(dfs(i+1,j), dfs(i,j+1))
            memo[i,j] = max(health-dungeon[i][j], 1)
            return memo[i,j]
        
        m, n = len(dungeon), len(dungeon[0])        
        memo = {} #min_init_HP required to reach certain cell
        return dfs(0,0)
"""        
single DP with 2D array
dp[i][j] = minimum health level required to reach the princess when entering (i, j)
https://leetcode.com/problems/dungeon-game/discuss/52826/a-very-clean-and-intuitive-solution-with-explanation
"""
class DP_Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])        
        minInitHP = collections.defaultdict(lambda:float('inf'))
        minInitHP[m,n-1] = 0
        minInitHP[m-1,n] = 0
        
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                minInitHP[i,j] = min(minInitHP[i+1,j], minInitHP[i,j+1]) - dungeon[i][j]
                minInitHP[i,j] = max(0, minInitHP[i,j]) #HP can't be negative
                    
        return minInitHP[0,0] + 1

"""
Double DP
Two arrays are used: one for saving minimum cost, one for saving minimum knight HP
https://leetcode.com/problems/dungeon-game/discuss/52784/Who-can-explain-why-%22from-the-bottom-right-corner-to-left-top.%22
"""
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])        
        minInitHP = collections.defaultdict(lambda:float('inf'))
        minCost = collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                if (i,j)==(0,0):
                    minCost[0,0] = dungeon[0][0]
                    minInitHP[0,0] = max(1, 1- minCost[0,0])
                else:
                    minCost[i,j] = dungeon[i][j] + max(minCost[i-1,j], minCost[i,j-1])
                    minInitHP[i,j] = min(
                        max(minInitHP[i-1,j], 1 - minCost[i-1,j] - dungeon[i][j]),
                        max(minInitHP[i,j-1], 1 - minCost[i,j-1] - dungeon[i][j]),
                        )
                    
        return minInitHP[m-1,n-1]
