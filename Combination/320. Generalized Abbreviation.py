class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper( pos, count, abbr ):
            if pos == len(word):
                # Once we reach the end, append current to the result
                result.append(abbr + str(count) if count > 0 else abbr)
            else:
                # Skip current position, and increment count
                helper( pos + 1, count + 1, abbr)
                # Include current position, and zero-out count
                helper( pos + 1, 0, abbr + (str(count) if count > 0 else '') + word[pos] )

        result = []
        helper(pos=0, count=0, abbr='')
        return result
