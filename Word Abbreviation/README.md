Divide and Conquer
Either (1) skip current position and increment count, or (2) include current position and make count 0

Once reach the end, append current to the result.
```
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper( pos, count, abbr ):
            countstr = str(count) if count>0 else ''
            if pos == len(word):
                result.append(abbr + countstr)
            else:
                helper( pos + 1, count + 1, abbr)
                helper( pos + 1, 0, abbr + countstr + word[pos] )

        result = []
        helper(pos=0, count=0, abbr='')
        return result
```
