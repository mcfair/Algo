"""
1. There are at least 1 and at most 1000 words.
2. All words will have the exact same length.
3. Word length is at least 1 and at most 5.
4. Each word contains only lowercase English alphabet a-z.
"""

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words: return []
        
        n = len(words[0])
        
        #create prefix hash map
        prefix = collections.defaultdict(list)
        for word in words:
            for i in range(1,n):
                prefix[word[:i]].append(word)
        
        #build word square using dfs
        squares = []
        def build(sq):
            if len(sq)==n:
                squares.append(sq)
                return
            
            m, pre = len(sq), ''
            for i in range(m):
                pre += sq[i][m]
                
            for word in prefix[pre]:
                build(sq+[word])
            
        for word in words:
            build([word])
        return squares
                
