def lowestBit(x):
  return x & -x
  
def highestBit(x):
  return 2**int(math.log(x,2))
 
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
       
    # Increment n by 1 so that 
    # there is only one set bit 
    # which is just before original 
    # MSB. n now becomes 1000000000 
    n = n + 1
   
    # Return original MSB after shifting. 
    # n now becomes 100000000 
    return n >> 1
#another explanation of power of 2 is hamming_weight=1  
def isPowerOfTwo(n):
  return n&(n-1)==0 if n>0 else False

def removeLowestBit(n):
  return n&(n-1) 
