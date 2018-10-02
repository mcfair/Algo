def toHex(self, num):
    if not num: return "0"
    mp = '0123456789abcdef'
    res = ''
    for i in xrange(8):
        n = num & 15
        c = mp[n]
        res = c + res
        num >>= 4
        if num == 0:
            break
    return res
