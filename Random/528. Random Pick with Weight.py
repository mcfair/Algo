"""
say we have the numbers 1, 5, 2 easiest solution is to construct the following array
arr[] = {0,1,1,1,1,1,2,2}
then generate a random number between 0 and 7 and return the arr[rnd]. 
This is solution is not really good though due to the space requirements it has (imagine a number beeing 2billion).

The solution here is similar but instead we construct the following array (accumulated sum)
{1, 6, 8} generate a number between 1-8 and say all numbers generated up to 1 is index 0. 
All numbers generated greater than 1 and up to 6 are index 1 and all numbers greater than 6 and up to 8 are index 2. 
After we generate a random number to find which index to return we use binary search.
"""
class Solution(object):
    def __init__(self, w):
        #cumulative sum
        self.w = list(itertools.accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
