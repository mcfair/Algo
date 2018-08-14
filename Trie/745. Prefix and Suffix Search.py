#O(nL^3) build hash table - 3 for loops O(nL^2) * concat string O(L)
#query takes O(1)
class WordFilter(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dic = collections.defaultdict(lambda: -1)
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                for j in range(len(word)+1):
                    self.dic[word[i:]+'_'+word[:j]] = weight
        #for k in self.dic: print (k)
       
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.dic[suffix+'_'+prefix]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
