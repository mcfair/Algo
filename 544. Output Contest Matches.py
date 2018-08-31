"""
Input: 8
Output: (((1,8),(4,5)),((2,7),(3,6)))
Explanation: 
First round: (1,8),(2,7),(3,6),(4,5)
Second round: ((1,8),(4,5)),((2,7),(3,6))
Third round: (((1,8),(4,5)),((2,7),(3,6)))
"""

class Solution(object):
    def findContestMatch(self, n):
        R = tuple(range(1, n+1))
        while len(R) > 2:
            R = tuple((R[i],R[~i]) for i in xrange(len(R)/2))
        return str(R).replace(' ','')
