"""
Three Methods:
DFS + Memo
Single DP from bottom-right corner to top-left corner
Double DP, maintain two matrix: minInitHP, currHP 
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
        
#single DP with 2D array
#dp[i][j] = minimum health level required to reach the princess when entering (i, j)
#https://leetcode.com/problems/dungeon-game/discuss/52826/a-very-clean-and-intuitive-solution-with-explanation
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
