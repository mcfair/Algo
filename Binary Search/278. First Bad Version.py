
def firstBadVersion(self, n):
    l, r = 1, n+1                  #search in [l, r) range
    while l<r:
        mid = (l+r)/2
        if isBadVersion(mid):
            r = mid
        else:
            l = mid+1
    return l
