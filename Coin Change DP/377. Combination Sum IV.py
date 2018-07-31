#It's actually permutation sum!
#different from coin change is that "sequence matters" - permutation


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """    
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            #dp[i] = sum([dp[i - c] for c in nums if i >= c])
            for c in nums:
                if i>=c:
                    dp[i]+=dp[i-c]
        return dp[-1]


#naive DFS solution TLE
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def permute(remain):
      
            if remain ==0:
                count[0]+=1
                return 
           
            for x in nums:
                if remain - x>=0:
                    permute(remain -x)
   
        count =[0]
        permute(target)
        return count[0]
