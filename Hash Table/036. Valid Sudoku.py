class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #just a different way of hashset
        seen = set()
        for i, row in enumerate( board):
            for j, x in enumerate(row):
                if x!='.':
                    for t in [(x,i,'-'),(x,'-',j),(x,i/3,j/3)]:
                        if t not in seen:
                            seen.add(t)
                        else:
                            return False
        return True
                    
