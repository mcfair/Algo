
def firstBadVersion(self, n):
    l, r = 1, n+1                  #search in [l, r+1) range, both r=n and r=n+1 works for this problem...
    while l<r:
        mid = (l+r)/2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid+1
    return l
