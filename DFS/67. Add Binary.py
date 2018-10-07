"""
Input: a = "11", b = "1"
Output: "100"

The time complex is O(m+n+c)，it's linear, where m=len(a)，n=len(b) and c="count of carries, which is less than min(m,n)".
"""
def addBinary(self, a, b):
    if not a or not b: 
        return a or b

    if a[-1] == '1' and b[-1] == '1':
        return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'

    elif a[-1] == '0' and b[-1] == '0':
        return self.addBinary(a[0:-1],b[0:-1])+'0'

    else:
        return self.addBinary(a[0:-1],b[0:-1])+'1'

