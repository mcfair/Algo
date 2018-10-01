#Alternating outputs, using heap

from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S):
       
        pq = []
        counts = Counter(S)
        for key, val in counts.items():
            heappush(pq, (-val, key))
        
        res = []
        tmp_cnt, tmp_key = 0, ''
        while pq:
            cnt, key = heapq.heappop(pq)
            res.append(key)
            if tmp_cnt < 0:
                heappush(pq, (tmp_cnt, tmp_key))
            tmp_cnt, tmp_key = cnt+1, key
    
        return ''.join(res) if len(res) == len(S) else ""
