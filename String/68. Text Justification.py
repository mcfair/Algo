"""
need a data structure to store the new row,
keep pushing word in and update the length
if the length > maxWidth, adjusting space inbetween words
"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words: 
            return []
        
        
        row , ans = [], []
        curlen = -1
        for word in words:
            if curlen+len(word)+1 < maxWidth:
                row.append(word)
                curlen+=len(word)+1 
            elif curlen+len(word)+1 == maxWidth:
                row.append(word)
                ans.append(' '.join(row))
                row = []
                curlen = -1
            else: #curlen+len(word)+1 > maxWidth:
                extraspaces = maxWidth - curlen
                if len(row) > 1:
                    d, m = divmod(extraspaces, len(row)-1)
                    justified_row = ''
                    for j, w in enumerate(row[:-1]):
                        nspaces = 1+ d + int(j<m)
                        justified_row += w + ' '*nspaces
                    ans.append(justified_row + row[-1])
                else:
                    ans.append(row[0]+' '*extraspaces)

                row = [word]
                curlen = len(word)       
        
        if row:
            lastrow = ' '.join(row)
            lastrow += ' '*(maxWidth - len(lastrow))
            ans.append(lastrow)
        return ans
        
        
