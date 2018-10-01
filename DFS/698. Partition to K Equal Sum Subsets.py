"""
Let's me further explain the two game changers in this solution:
1, if sums[j] == 0: break
"empty bucket" pruning
The key is, sums[j] == 0 means for all k > j, sum[k] == 0; because this algorithm always fill the previous buckets before trying the next.
So if by putting nums[i] in this empty bucket can't solve the game, putting nums[i] on other empty buckets can't solve the game too.

2, nums.sort(reverse=True)
Always start from big numbers for this kind of question, just by doing it yourself for a few times you will find out that the big numbers are the easiest to place.
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        
        S = sum(nums)
        if S%k: return False
        
        subsum = S/k
        sums = [0]*k
        nums.sort(reverse=True)
        l = len(nums)
        
        def walk(i):
            if i == l:
                return len(set(sums)) == 1
            for j in xrange(k):
                sums[j] += nums[i]
                if sums[j] <= subsum and walk(i+1):
                    return True
                sums[j] -= nums[i]
                if sums[j] == 0: #"empty bucket" pruning
                    break
            return False        
        
        return walk(0)
