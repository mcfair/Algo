
def toHex(self, num):
    if num==0: return '0'
    
    table, res = '0123456789abcdef', ''
    i = 0
    while num and i<8:
        res = table[num & 0xF] + res #take last for bits and add to the left
        num = num>>4
        i +=1
    return res
