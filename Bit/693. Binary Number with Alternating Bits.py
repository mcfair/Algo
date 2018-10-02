"""
def highestBit2(x):
    # Suppose n is 273 (binary  
    # is 100010001). It does following 
    # 100010001 | 010001000 = 110011001 
    n |= n>>1
    # 110011001 | 001100110 = 111111111 
    n |= n>>2   
    n |= n>>4  
    n |= n>>8
    n |= n>>16
"""

#if it's alternating 1s and 0s, n^(n>>1) should give 000011...1
#use highest bit trick to generate that number, and compare to n^(n-1)
def hasAlternatingBits(self, n):
    h = n
    for i in range(5):
        h |= h>>1  
    return h == n^(n>>1)

#slower, go bit by bit
def hasAlternatingBits(self, n):

    while n:
        prev_bit = n&1
        n = n>>1
        if (n&1) + prev_bit != 1:
        #if (n&1) ^ prev_bit !=1:
        #if not (n&1) ^ prev_bit
            return False

    return True
