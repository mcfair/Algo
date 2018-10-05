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

