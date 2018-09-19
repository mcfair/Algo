
#Note that the similarity relation is not transitive in the original question.
#So this problem can't be solved by union-find, as it asserts transitivity.
#Code actually solves 737. Sentence Similarity II

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
        #for k,v in dic.items(): print k,v
        

        for w1,w2 in zip(words1,words2):
            #print w1,w2, isSimilar(w1,w2)
            if not isSimilar(w1,w2):
                return False
        return True
