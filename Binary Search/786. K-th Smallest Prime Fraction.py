"""
Binary Search + Counting(looped binary search)
"""
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        l, r = 0, 1
        p, q = 0, 1
        n = len(A)
        while l<r:
            mid = (l+r)*0.5
            
            count = 0
            pairIndex = []
            for i in range(n):
                #find elements that satisfies A[i]/A[j] < mid, rewrite it as  A[j] > A[i]/mid
                #we can use bisect_right to find insertion point "j"
                j = bisect.bisect_right(A, A[i]*1.0/mid) 
                #the right half is n-j
                count +=  n - j
                pairIndex.append((i,j))
                
            if count < K:
                l = mid 
            elif count > K:
                r = mid
            else:
                pairs = [(A[i], A[j]) for i, j in pairIndex if j < n]
                return max(pairs, key=lambda x: x[0]*1.0 / x[1])
            
            
#Use heap to make code cleaner.            
def kthSmallestPrimeFraction(self, A, K):
    l, r = 0, 1
    p, q = 0, 1
    n = len(A)
    while l<r:
        mid = (l+r)*0.5
        count = 0
        pairs = []
        for i in range(n):
            j = bisect.bisect_right(A, A[i]*1.0/mid) 
            count +=  n - j
            if j<n: 
                heapq.heappush(pairs, (-1.0*A[i]/A[j],A[i],A[j]))

        if count < K:
            l = mid #since we have a "else" statement, mid+1 doesn't work here
        elif count > K:
            r = mid
        else:
            return heapq.heappop(pairs)[1:]
