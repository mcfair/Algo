#Bi-directional BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        front = set([beginWord])
        back = set([endWord])
        words = set(wordList)
        
        if endWord not in words: return 0
       
        words -= front 
        
        dist = 1
        while front:
            tmp = []
            for word in front:
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        nxtword = word[:i]+char+word[i+1:]
                        if nxtword in words:
                            tmp.append(nxtword)
           
            front = set(tmp)
            
            dist += 1
            if front & back:
                return dist
            if len(back) < len(front):
                front, back = back, front
            words -= front    
        return 0
        
#with hashtable, but not really speeding up in OJ
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        front = set([beginWord])
        back = set([endWord])
        words = set(wordList)
        
        if endWord not in words: return 0
        
        dic = collections.defaultdict(list)
        for word in words:
            for i in range(len(word)):
                dic[word[:i]+'_'+word[i+1:]].append(word)
        
        words -= front 
        dist = 1
        while front:
            tmp = []
            for word in front:
                for i in range(len(word)):
                    for nxtword in dic[word[:i]+'_'+word[i+1:]]:
                        if nxtword in words:
                            tmp.append(nxtword)
           
            front = set(tmp)
            
            dist += 1
            if front & back:
                return dist
            if len(back) < len(front):
                front, back = back, front
            words -= front    
        return 0
        
