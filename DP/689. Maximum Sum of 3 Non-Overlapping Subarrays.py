#First get the rangeSum array, call it W, then the problem reduced to:
#Given some array W and an integer K, what is the lexicographically smallest tuple of indices (i, j, k) 
#with i + K <= j and j + K <= k that maximizes W[i] + W[j] + W[k]?

#We can take a similar approach to Largest Area in Histogram problem.
#Find the "so far" max from the left, O(n)
#Find the "so far" max from the right, O(n)
#Traverse through the array again to find maxsum(i,j,k), O(n)
#Successfully reduce time from O(n^3) to O(n)

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k*3 > len(nums): raise ValueError('K is too large')
        if k*3 == len(nums): return sum(nums)
 
        #calculate the window k sum
        ksum = [sum(nums[:k])]
        for i in range(1,len(nums)-k+1):
            ksum += [ksum[-1]+nums[i+k-1]-nums[i-1]]
        
        #store the index of max ksum "so far", counting from the left 
        left = [0]*len(nums)
        maxsum, maxi = -sys.maxint, 0
        for i in range(0,len(nums)-k+1):
            if ksum[i]>maxsum:  # ">" from left to make sure lexicographical order
                maxsum, maxi = ksum[i], i
            left[i] = maxi
            
        #store the index of max ksum "so far", counting from the right (reverse)
        right = [0]*len(nums)
        maxsum = -sys.maxint
        for i in range(len(nums)-k, -1, -1):
            if ksum[i]>=maxsum:   # ">=" from right to make sure lexicographical order
                maxsum, maxi = ksum[i], i
            right[i] = maxi
        
        #varying j to find the maxsum
        maxsum, ret = -sys.maxint, None
        for j in range(k, len(nums)-2*k+1):
            newsum = ksum[left[j-k]]+ ksum[j] +ksum[right[j+k]]
            if newsum > maxsum:
                maxsum = newsum
                ret = left[j-k], j, right[j+k]
        return ret          
        
    
 #brutal force, TLE
 class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
 
        if k*3 > len(nums): raise ValueError('too big k')
        if k*3 == len(nums): return sum(nums)
        
        curmax = 0
        curans = None
        
        rsum = [0]
        for x in nums:
            rsum.append(x+rsum[-1])
        for i in range(len(rsum)-k):
            rsum[i] = rsum[i+k] -rsum[i]
        
        
        for i in range(len(nums)-3*k+1):
            for j in range(i+k, len(nums)-2*k+1):
                for l in range(j+k, len(nums)-k+1):
                    
                    sums = rsum[i] +  rsum[j] + rsum[l]
                    if sums > curmax:
                        curmax = sums
                        curans = (i,j,l)
                    
        return curans
        
