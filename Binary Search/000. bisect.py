def bisect_left(a, target, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in
    a[i:] have e >= x.  So if x already appears in the list, a.insert(x) will
    insert just before the leftmost x already there.
    Optional args lo (default 0) and hi (default len(a))
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] < target: 
            lo = mid+1
        else: 
            hi = mid
    return lo

def bisect_right(a, target, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e <= x, and all e in
    a[i:] have e > x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.
    Optional args lo (default 0) and hi (default len(a))  
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid] > target: 
            hi = mid
        else: 
            lo = mid+1
    return lo

## Another implementation using hi=len(a)-1, instead of hi=len(a)

def bisect_left(nums, target):
    l, r = 0, len(nums) -1
    while l < r:
        m = (l + r) / 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l if nums[l] == target else -1

def bisect_right(nums, target):
    l, r = 0, len(nums) -1
    while l < r:
        m = (l + r) / 2 + 1  # Make mid biased to the right
        if nums[m] > target:
            r = m - 1
        else:
            l = m
    return l if nums[l] == target else -1
