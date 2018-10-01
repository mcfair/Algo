from collections import Counter
from heapq import heappop, heappush

class Solution(object):
    def rearrangeString(self, s, k):
        
        if k == 0: return s        
        
        pq = []
        for char, freq in Counter(s).items():
            heappush(pq,  (-freq, char))
         
        res = [] #list is fast than concatenating string
        tmp = []
        while len(pq)>=k:
            for _ in range(k): 
                freq, char = heappop(pq)
                res.append(char)
                if freq+1 < 0:
                    tmp.append((freq+1, char))     
            while tmp:
                heappush(pq, tmp.pop())
        while pq:
            freq, char = heappop(pq)
            res.append(char)
        return ''.join(res) if len(res) == len(s) else ""
