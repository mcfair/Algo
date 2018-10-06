
#two pointers
#O(n)
def findMaxAverage(self, nums, k):
    windowsum = sum(nums[:k])
    maxsofar = windowsum
    l, r = 0, k
    while r < len(nums):
        windowsum += nums[r] - nums[l]

        maxsofar = max(maxsofar,  windowsum)
        l, r = l+1, r+1

    return maxsofar/float(k)
    
#one pointer
#This is a fixed size window, why do we need two pointer....
#O(n)
def findMaxAverage(self, nums, k):
    maxn = sum(nums[:k])
    temp = maxn
    for i in range(len(nums) - k):
        temp = temp - nums[i] + nums[i + k]
        maxn = max(maxn, temp)
    return maxn / float(k)

"""
Followup question is "what if window size >= k", instead of a fixed k.
644. Maximum Average Subarray II
Brutal Force solution is O(n*(n-k)) = O(n^2)
Binary Search is O(nlogn), intuition is that answer lies between min(nums) and max(nums).
Inside binary search, the question we need to answer is: Is there a subarray of length>=k with average >= "mid"?
The algorithm to answer this question is O(n).
nums[i]+...+nums[j] >= mid * (j-i+1) is equivalent to (nums[i]-mid)+ .. +(nums[j]-mid) >=0
if this holds True, left = mid +tol, else: right = mid
"""

def findMaxAverage(self, nums, k):
    #check whether there is (nums[i]-mid)+ .. +(nums[j]-mid) >=0 for any i<j and j-i+1 >= k
    def checkIfThereIsLargerAverage(mid):
        a = [x-mid for x in nums]      #a is diff array
        curr = sum(a[:k])              #initial sum of window size k
        if curr >= 0: 
            return True

        prev = 0
        for i in range(k,len(nums)):   
            curr += a[i]               #current largest sum upto index i (with window size >=k)
            prev += a[i-k]             #prefix sum of a[0...i-k]
            if prev < 0:               #if prev sum < 0, curr sum can be larger
                curr -=prev
                prev = 0
            if curr >= 0:              
                return True

        return False
    
    #Binary Search
    l, r, tol = min(nums), max(nums), 1e-5
    while l+1e-5 < r:
        mid = (l+r)*0.5
        if checkIfThereIsLargerAverage(mid):
            l = mid + tol
        else:
            r = mid
    return l
        
