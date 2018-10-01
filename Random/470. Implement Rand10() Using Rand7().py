"""
straight-forward solution, 
use two rand7 to represent range 1~49 (Note that rand7+rand7 can't represent 1~14 uniformly)
if num <=40, return num%10+1
The average call of rand7 is 2 * 49 / 40 = 2.45
"""

class Solution(object):
    def rand10(self):
        res = 41
        while res > 40:
            res = (rand7()-1)*7 + rand7()
        return res%10+1

   
#most optimized way
#https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C++JavaPython-Average-1.199-Call-rand7-Per-rand10

class Solution(object):
    def __init__(self):
        self.cache = []
        
    def rand10(self):
        while not self.cache: 
            self.generate()
        return self.cache.pop()

    def generate(self):
        n = 19  
        curnum = sum((rand7() - 1) * (7**i) for i in range(n))
        rang = 7 ** n
        while curnum < rang / 10 * 10:
            self.cache.append(curnum % 10 + 1)
            curnum /= 10
            rang /= 10
