"""
Divide a by b, without using multiplication, division and mod operators.
Integer division should truncate toward zero.
"""
def divide(self, a, b):
    sign = (a < 0) ^ (b < 0)
    a, b, res = abs(a), abs(b), 0
    while a >= b:
        x = 0
        while a >= b << (x + 1): 
          x += 1
        res += 1 << x
        a -= b << x
    return min(res if sign else -res, 2147483647)
