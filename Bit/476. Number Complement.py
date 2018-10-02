def findComplement(self, num):
        comp = loc = 0
        while num:
            bit = num & 2**loc     #find bit at each location
            num -= bit            
            comp += bit^2**loc     #toggle bit 0/1, and add to complement
            loc +=1
        return comp
        
        
int findComplement(int num) {
    int mask = num;
    mask |= mask >> 1;
    mask |= mask >> 2;
    mask |= mask >> 4;
    mask |= mask >> 8;
    mask |= mask >> 16;
    return num ^ mask;
}
