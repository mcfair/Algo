#Divide and Conquer
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """ 
        if input.isdigit():
            return [int(input)]
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul} 
    
        res = []
        for i in xrange(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for left in res1:
                    for right in res2:
                        res.append(ops[input[i]](left,right))
        return res
