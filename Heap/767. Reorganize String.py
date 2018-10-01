#Alternating outputs, using heap

from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, S):
        res = ""
        pq = []
        counts = Counter(S)
        for key, val in counts.items():
            heappush(pq, (-val, key))
        
        tmp_cnt, tmp_key = 0, ''
        while pq:
            cnt, key = heapq.heappop(pq)
            res += key
            if tmp_cnt < 0:
                heappush(pq, (tmp_cnt, tmp_key))
            cnt += 1
            tmp_cnt, tmp_key = cnt, key
        
        if len(res) != len(S): return ""
        return res
