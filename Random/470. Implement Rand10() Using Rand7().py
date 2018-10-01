"""
straight-forward solution, 
use rand7 to represent range 1~49
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
