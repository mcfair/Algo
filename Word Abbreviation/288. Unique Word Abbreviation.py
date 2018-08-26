class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abtable = collections.defaultdict(set)
        for word in dictionary:
            if len(word)>2:
                abbr = word[0] + str(len(word)-2) + word[-1]  
            else:
                abbr = word
            self.abtable[abbr].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        abbr = word[0] + str(len(word)-2) + word[-1] if len(word)>2 else word
        return len(self.abtable[abbr])==0 or len(self.abtable[abbr])==1 and word in self.abtable[abbr]
        
