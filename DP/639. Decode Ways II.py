class Solution(object):


    def numDecodings(self, s):
        
        M = 10**9 + 7
        
        one = collections.defaultdict(int) 
        one.update({str(i): 1 for i in range(1, 10)})
        one.update({'*': 9, '0': 0})

        two = collections.defaultdict(int) 
        two.update({str(i): 1       for i in range(10, 27)})
        two.update({'*' + str(i): 2 for i in range(0,7)})
        two.update({'*' + str(i): 1 for i in range(7,10)})
        two.update({'1*': 9, '2*': 6, '**': 15})
        
        prev, cur = 1, one[s[0]]
        
        for i in range(1, len(s)):
            prev, cur = cur, (cur*one[s[i]] + prev*two[s[i-1:i+1]])%M
        return cur
    
