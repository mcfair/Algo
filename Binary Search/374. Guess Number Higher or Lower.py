def guessNumber(self, n):
    l, r = 1, n 
    mid = (l+r)/2
    while guess(mid)!=0:
        if guess(mid)==1:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l+r)/2

    return mid

"""
Follow-up question LC375. Guess Number Higher or Lower II
It is actually not DP problem instead of binary search.
It's typical in interview that follow-up question can't be solved by refactoring code.
Instead you need to start over again, like we saw in Google on-site: 
orgininal question can be solved by sliding window, follow-up is a 2D DP
"""
