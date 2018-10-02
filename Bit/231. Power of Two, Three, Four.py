
def isPowerOfTwo(self, n):
    #return n&(n-1)==0 if n >0 else False
    return n>0 and n&(n-1)==0 


def isPowerOfThree(self, n):
    if n<=0: 
        return False
    while n%3 ==0: 
        n = n/3
    return n==1

"""
in binary representation
power of 2 would be "1" followed by any number of "0"
power of 4 would be "1" followed by EVEN number of "0"
#return num>0 and num&(num-1)==0 and len(bin(num)[3:])%2==0

Another way is to design a mask to filter out non power of 4s
0101 0101 0101 0101 0101 0101 0101 0101 = 0x55555555
"""
def isPowerOfFour(self, num):
    return num>0 and num&(num-1)==0 and num & 0x55555555 == num
