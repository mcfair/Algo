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
