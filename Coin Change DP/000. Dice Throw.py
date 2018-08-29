"""
Questions: 
Given N dice each with M faces, numbered from 1 to M, find the number of ways to get sum X. 
X is the summation of values on each face when all the dice are thrown.

Idea:
Coin Change with limitation

Time complexity is O(NMX)
"""
def numOfWays(N, M, X):
    ways = [[0]*(X+1) for _ in range(N)]
    for i in range(1, min(M,X)+1):
       ways[1][i] =1
      
    for i in range(2, N):
       for x in range(1, X):
          for k in range(1, M):
             if k<j:
               ways[i][b] += ways[i-1][b-k]
    return ways[N][X]
 
