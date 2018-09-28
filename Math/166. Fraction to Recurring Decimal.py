class Solution:
    def fractionToDecimal(self, a, b):
        """
        :type a is numerator: int
        :type b is denominator: int
        :rtype: str
        """
        if a%b==0: return str(a//b)
        res = '-' if a/b < 0 else ''
        a, b = abs(a), abs(b)
        
        div, a = divmod(a,b)
        res += str(div)+'.'

        record = {}
        while a!=0:
            if a not in record:
                record[a] = len(res)
            else:
                i = record[a]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            div, a = divmod(a*10, b)
            res+=str(div)

        return res
