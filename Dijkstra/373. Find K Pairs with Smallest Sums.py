# BFS+Heap,  not Dijkstra Algo
# O(k*logk) time
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
 
        m, n = len(nums1), len(nums2)
        if not m or not n: return []
        
        ans = []
        visited = set([])
        q = [(nums1[0]+nums2[0], 0, 0)]
        
        while len(ans)<k and q:
            _, i,j = heapq.heappop(q)
            #visited.add((i,j))   #adding visited here is wrong, because q may stack duplicated ones before pop out.
            ans.append([nums1[i],nums2[j]])
            if len(ans)==k:
                return ans
            if i+1<m and (i+1,j) not in visited:
                heapq.heappush(q, (nums1[i+1]+nums2[j], i+1,j))
                visited.add((i+1,j))
            if j+1<n and (i,j+1) not in visited:
                heapq.heappush(q, (nums1[i]+nums2[j+1], i,j+1))
                visited.add((i,j+1))
        return ans
