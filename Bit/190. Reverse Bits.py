#Google!
"""
take 8 bit binary number abcdefgh for example, the process is as follow:

abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
"""
#design bitmask for swapping
def reverseBits(n):
    n = (n >> 16) | (n << 16)
    n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)  
    n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)  #1100 >>2,  0011 <<2
    n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)  #1010 >>1,  0101 <<1
    return n

#take out bit one by one and stack into res 
def reverseBits(self, n):
    res=0
    for i in range(32):
        res=(res<<1)+(n&1) 
        n=n>>1
    return res 
