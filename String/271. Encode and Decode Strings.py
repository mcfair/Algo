"""
Thinking
We ought to define a delimiter to separate words within the list, however, any delimiter can be part of the original word. Thus, we use lengthOfStr + : as prefix to delimit a word 
"""
class Codec:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
