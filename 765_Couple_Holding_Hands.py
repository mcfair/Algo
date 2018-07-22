



#greedy algo O(n^2) time O(1) space, 20ms beats 100%
#but how is it getting min # of swaps, not greater?
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        def couple(x):
            return x-1 if x%2 else x+1
        
        nswap = 0
        for i in range(0,len(row),2):
            c = couple(row[i])
            if row[i+1]!=c:
                j = i+2
                while j< len(row):
                    if row[j]==c:
                        nswap +=1
                        row[j], row[i+1] = row[i+1],row[j]
                        break
                    j+=1
        return nswap
                
