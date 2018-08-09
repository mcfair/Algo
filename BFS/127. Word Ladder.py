#Bi-directional BFS

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        front, back, wordList = set([beginWord]), set([endWord]), set(wordList)
        if endWord not in wordList: return 0
        
        wordList.discard(beginWord)
        
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                dic[word[:i] + "_" + word[i+1:]].append(word)
                
        dist = 2
        while front:
            front =  set(reduce(lambda x,y:x+y, 
                                [dic[word[:i] + '_'+word[i+1:]] for word in front for i in range(len(word))]))
            
            if front & back:
                return dist
            dist+=1
            if len(front) > len(back):
                front, back = back, front
            wordList -=front
        
        return 0
