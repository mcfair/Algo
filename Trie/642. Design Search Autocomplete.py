class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word, freq):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        
        if '$' not in curr:
            curr['$'] = -freq
            curr['#']=word
        else:
            curr['$'] -= freq
        
    def search(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr:
                return []
            curr = curr[c]
        return self.dfs(curr)
    
    def dfs(self, root):
        #return all autocomplete words
        ret = []
        if '#' in root:
            ret.append([root['$'], root['#']])
        for c in root:
            if c not in{'$','#'}:
                ret.extend(self.dfs(root[c]))
        return ret
    
class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        
        self.trie = Trie()
        for i in range(len(times)):
            self.trie.insert(sentences[i], times[i])
          
        self.curr = self.trie.root
        self.text = ''
        
    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """    
        if c!='#':
            self.text += c
            return [x[1] for x in sorted(self.trie.search(self.text))[:3]]
            
        else:
            self.trie.insert(self.text,  1)
            self.text=''
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
