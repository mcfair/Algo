"""
Treat the first N - |B| numbers as those we can pick from. 
Iterate through the blacklisted numbers and map each of them to to one of the remaining non-blacklisted |B| numbers

For picking, just pick a random uniform int in 0, N - |B|. 
If its not blacklisted, return the number. 
If it is, return the number that its mapped to.
"""

import random
class Solution:
    def __init__(self, N, blacklist):
        blacklist = sorted(blacklist)
        self.b = set(blacklist)
        self.m = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self):
        i = random.randint(0, self.length - 1)
        return self.m[i] if i in self.m else i
