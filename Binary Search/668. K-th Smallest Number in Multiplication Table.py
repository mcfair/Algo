
"""
Binary Search + Count

Intuitively we can write "Count" like below
count = sum(bisect.bisect_right(range(1,n+1), mid/i) for i in range(1,m+1)) #BTW, this will TLE 

For this particular problem, we know each row is [1, 2, 3, .., n]*i 
If there are x number of elements less than mid, it satisfies x < mid/i, so x <= mid/i
So the count of each row is simply min(mid/i, n)
"""
 
def findKthNumber(self, m, n, k):

    l, r = 1, m*n
    while l<r:
        mid = (l+r)/2

        #see explanation
        count = sum(min(mid/i, n) for i in range(1,m+1))

        if count < k:
            l = mid+1
        else:
            r = mid
    return l
