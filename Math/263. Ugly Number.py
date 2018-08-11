#Easy
"""
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
"""

class Solution(object):
    def isUgly(self, num):
        for p in [2,3,5]:
            while num>1 and num%p==0:
                num/=p
        return num==1
