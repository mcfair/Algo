#Divide and Conquer
class Solution(object):
    def __init__(self):
        self.ops = {'+': operator.add, '-': operator.sub, '*': operator.mul} 
    
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """ 
        if input.isdigit():
            return [int(input)]

        res = []
        for i, c in enumerate(input):
            if c in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for left in res1:
                    for right in res2:
                        res.append(self.ops[c](left,right))
        return res
