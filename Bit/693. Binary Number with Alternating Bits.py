#use highest bit trick
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
