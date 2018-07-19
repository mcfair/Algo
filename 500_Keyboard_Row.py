class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        
        Key is to use hashset O(1) query, O(|w|) issubset
        """

        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                ret.append(word)
        return ret 
