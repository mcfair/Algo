#Stefan's solution, only push index in, keep track of window size
"""
The indexes in deque are from the current window, they're increasing, and their corresponding nums are decreasing. 
Then the first deque element is the index of the largest window value.

For each index i (when >= k-1):

Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.
Popleft (from the front) the index i - k, if it's still in the deque (it falls out of the window).
Append the current window maximum (leftmost) to the output.
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        maxval = []
        
        for i, x in enumerate(nums):
            # the next 3 lines are the "push" operation
            while dq and nums[dq[-1]] < x:
                dq.pop()
            dq.append(i)
            
            #current window is [i-k+1, i] inclusive
            if dq[0] == i - k:
                dq.popleft()
                
            #first valid window of size k is [0, k-1], so first valid i is k-1
            if i >= k - 1:
                maxval.append(nums[dq[0]])
                
        return maxval

    
    
#Huahua's solution, only push value in, keep track of window size
class MaxQueue(object):
    def __init__(self):
        self.q_ = collections.deque()

    def push(self, e):
        while self.q_ and e > self.q_[-1]: 
            self.q_.pop()
        self.q_.append(e)

    def pop(self):
        self.q_.popleft()

    def max(self):
        return self.q_[0]
    
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        
        if not nums: return []
        
        q = MaxQueue()
        
        #preload first k-1 items, no pop
        k = min(k, len(nums))
        for i in range(k-1):
            q.push(nums[i])
         
        #calculate moving max 
        ans = []
        for i in range(k-1, len(nums)):
            q.push(nums[i])
            ans.append(q.max())
            if nums[i - k + 1] == q.max(): 
                q.pop()
        return ans

    
#Another solution, keep track of value and distance/count
class Monoqueue:
    def __init__(self):
        self.dq = collections.deque()
        #each item in the dqueue is [val, dist]
        #val: the actual value, 
        #dist: distance (how many elements were deleted) between it and the one before it. 
        #distance of the leftmost element (the max) in dq means the distance between the max and the window left boundary

    def push(self, val):
        count = 0
        while len(self.dq) > 0 and self.dq[-1][0] < val:
            count += self.dq[-1][1] + 1
            self.dq.pop()
        self.dq.append([val, count])   

    def getMax(self):
        return self.dq[0][0]

    def pop(self):
        if self.dq[0][1] > 0:
            self.dq[0][1] -= 1
            return
        self.dq.popleft()
        
        
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if len(nums) < 1:
            return []
   
        mq = Monoqueue()

        k = min(k, len(nums))
        
        #preload first k-1 items
        for ii in range(k-1):
            mq.push(nums[ii])
            print "push" , nums[ii], mq.dq
        
        #get the moving max for all sliding windows.
        maxval = []
        for ii in range(k-1 , len(nums)):
            mq.push(nums[ii])            #push the item
            print "push" , nums[ii], mq.dq, "window= %d - %d"%(ii-k+1, ii)
            maxval.append(mq.getMax())   #get the max for the window
            print "pop" , nums[ii], mq.dq,"window= %d - %d"%(ii-k+1, ii)
            mq.pop()                     #pop the first item
          
        return maxval
"""
Input: nums=[1,3,-1,-3,5,3,6,7], k=3

Output:
push 1 deque([[1, 0]])
push 3 deque([[3, 1]])
push -1 deque([[3, 1], [-1, 0]]) window= 0 - 2
pop -1 deque([[3, 1], [-1, 0]]) window= 0 - 2
push -3 deque([[3, 0], [-1, 0], [-3, 0]]) window= 1 - 3
pop -3 deque([[3, 0], [-1, 0], [-3, 0]]) window= 1 - 3
push 5 deque([[5, 2]]) window= 2 - 4
pop 5 deque([[5, 2]]) window= 2 - 4
push 3 deque([[5, 1], [3, 0]]) window= 3 - 5
pop 3 deque([[5, 1], [3, 0]]) window= 3 - 5
push 6 deque([[6, 2]]) window= 4 - 6
pop 6 deque([[6, 2]]) window= 4 - 6
push 7 deque([[7, 2]]) window= 5 - 7
pop 7 deque([[7, 2]]) window= 5 - 7
"""
