"""
Three Methods:
DFS + Memo
Single DP from bottom-right corner to top-left corner
Double DP, maintain two matrix: minInitHP, currHP 
"""
class DFSSolution(object):
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
        
