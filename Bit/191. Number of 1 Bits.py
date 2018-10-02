#shift bit by bit
def hammingWeight(self, n):
    cnt = 0
    while n:
        cnt += n & 1
        n = n>>1
    return cnt

#skip 0s, and jump to lowest bit everytime
def hammingWeight(self, n):
    cnt = 0
    while n:
        n = n&(n-1)  #remove the lowest bit
        cnt+=1
    return cnt
    
    
#recursive way
def hammingWeight(self, n):
    if n<=0: return 0
    return 1+ self.hammingWeight(n&(n-1)) 
    # return 1+ self.hammingWeight(n&(n-1)) if n>0 else 0    
