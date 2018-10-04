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
