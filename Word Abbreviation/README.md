Divide and Conquer
Either (1) skip current position and increment count, or (2) include current position, and zero-out count
Once reach the end, append current to the result.
```
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper( pos, count, abbr ):
            if pos == len(word):
                result.append(abbr + str(count) if count > 0 else abbr)
            
            else:
                helper( pos + 1, count + 1, abbr)
                helper( pos + 1, 0, abbr + (str(count) if count > 0 else '') + word[pos] )

        result = []
        helper(pos=0, count=0, abbr='')
        return result
```
