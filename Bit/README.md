
```python
def lowestBit(x):
  return x & -x
  
def removeLowestBit(n):
  return n&(n-1) 
  
def isPowerOfTwo(n):
  return n&(n-1)==0 if n>0 else False

def highestBit(x):
  return 2**int(math.log(x,2))

def highestBit2(x): 
    n |= n>>1 
    n |= n>>2   
    n |= n>>4  
    n |= n>>8
    n |= n>>16
       
    # Increment n by 1 so that 
    # there is only one set bit 
    # n now becomes 1000000000 
    n = n + 1
   
    # Return original MSB after shifting right
    return n >> 1 

```
