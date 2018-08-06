#Such an elegant solution & beautiful code
#O(n^2) time & O(n^2) space

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        #create set of tuples for O(1) query  
        banned = set(map(tuple, mines))
        
        #use one matrix to keep track the shortest arm of (left, right, up, down)
        dp = [[0] * N for _ in xrange(N)]
        
        #count horizontally O(n^2)
        for r in xrange(N):
            count = 0 #left arm
            for c in xrange(N):
                count = 0 if (r,c) in banned else count+1
                dp[r][c] = count
            
            count = 0 #right arm
            for c in xrange(N-1, -1, -1):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        #count vertically O(n^2)
        for c in xrange(N):
            count = 0 #down arm
            for r in xrange(N):
                count = 0 if (r,c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
              
            count = 0 #up arm
            for r in xrange(N-1, -1, -1):
                count = 0 if (r, c) in banned else count+1
                if count < dp[r][c]: dp[r][c] = count
        
        # max of max O(n^2)
        return max(map(max,dp))
