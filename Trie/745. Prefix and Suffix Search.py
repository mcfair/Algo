#balanced solution for build and query
#build O(nL^2)
#query O(L)
class Trie(object):
    def __init__(self):
        self.root = {}
    def insert(self, word, weight):
        cur = self.root
        for c in word:
            cur = cur.setdefault(c,{})
            cur['$']= weight
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                return -1
            cur = cur[c]
        return cur['$']
    
class WordFilter(object):
    
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                self.trie.insert(word[i:]+'_'+word, weight)
     
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.trie.search(suffix+'_'+prefix)
    
#solution for fast query    
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
       
    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        return self.dic[suffix+'_'+prefix]


 )
