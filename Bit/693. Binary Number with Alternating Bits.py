
def hasAlternatingBits(self, n):

    while n:
        prev_bit = n&1
        n = n>>1
        if (n&1) + prev_bit != 1:
            return False

    return True
