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
        self.dqueue = []
        #each item in the dqueue is [val, dist]
        #val: the actual value, 
        #dist: distance (how many elements were deleted) between it and the one before it. 
        #0 distance means right next to each other

    def push(self, val):
        count = 0
        while len(self.dqueue) > 0 and self.dqueue[-1][0] < val:
            count += self.dqueue[-1][1] + 1
            self.dqueue.pop()
        self.dqueue.append([val, count])   

    def getMax(self):
        return self.dqueue[0][0]

    def pop(self):
        if self.dqueue[0][1] > 0:
            self.dqueue[0][1] -= 1
            return
        self.dqueue.pop(0)
        
        
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
            print "push" , nums[ii], mq.dqueue
        
        #get the moving max for all sliding windows.
        maxval = []
        for ii in range(k-1 , len(nums)):
            mq.push(nums[ii])            #push the item
            maxval.append(mq.getMax())   #get the max for the window
            mq.pop()                     #pop the first item
          
        return maxval
