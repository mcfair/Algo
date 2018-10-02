
def isPowerOfTwo(self, n):
    return n&(n-1)==0 if n >0 else False
