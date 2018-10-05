"""
Use Python built-in functions, TLE
"""

def smallestDistancePair(self, nums, k):
    q = []
    for a,b in itertools.combinations(nums, 2):
        heapq.heappush(q, abs(a-b))

    for _ in range(k):
        v = heapq.heappop(q)
    return v

"""
Binary Search inside binary search
"""
def smallestDistancePair(self, nums, k):

    nums.sort() 
    n = len(nums)
    #search on the diffrence space, not on nums
    lo, hi = 0, nums[-1] - nums[0]

    while lo<hi:
        mid = (lo+hi)//2

        count = 0
        for i in range(n):
            j = bisect.bisect_right(nums, nums[i]+mid)
            count += j-i-1

        if count < k:
            lo = mid+1
        else:
            hi = mid

    return lo

                
            
