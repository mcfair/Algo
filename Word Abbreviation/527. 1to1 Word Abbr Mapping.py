
class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
 
        def shorten(word, k):
            if len(word) - 1 -k <= 1:
                return word
            else:
                return word[:k] + str(len(word)-1-k) + word[-1]
        
        n = len(words)
        abbr =[''] * n    #store abbreviation for each word
        prefix = [1] * n  #number of char as prefix
        dups = collections.defaultdict(list) #duplicates = {abbr: [index1, index2, ... ]}
        
        for i,word in enumerate(words):
            abbr[i] = shorten(word,1)
            dups[abbr[i]].append(i)
        
        
        for i in range(n):
            if len(dups[abbr[i]]) == 1:
                continue
            else:
                while len(dups[abbr[i]]) > 1:
                    for index in dups[abbr[i]]:
                        prefix[index]+=1
                        newabbr = shorten(words[index], prefix[index])
                        abbr[index] = newabbr
                        dups[newabbr].append(index)
       
        return abbr
    
   
            
        
