class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        def isSimilar(w1,w2):
            if w1==w2:
                return True
            if w1 in dic:
                return w2 in dic[w1]
            if w2 in dic:
                return w1 in dic[w2]
            return False
        
        if len(words1)!=len(words2):
            return False
        
        dic = collections.defaultdict(set)
        for a, b in pairs:
            dic[a].add(b)
            dic[b].add(a)
   
        for w1,w2 in zip(words1,words2):
            if not isSimilar(w1,w2):
                return False
        return True
        
