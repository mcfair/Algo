def singleNumber2(self, nums):
    a=b=0
    for x in nums:
        b = b^x & ~a
        a = a^x & ~b
    return a|bc
