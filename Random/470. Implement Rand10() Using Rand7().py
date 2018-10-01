#straight-forward solution, use rand7 to represent rand49
#return rand40%10 + 1

class Solution(object):
    def rand10(self):
        res = 41
        while res > 40:
            res = (rand7()-1)*7 + rand7()
        return res%10+1
