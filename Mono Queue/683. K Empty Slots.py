# -Method 1- My Mono Queue Algorithm O(n)

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if k <0  or k > len(flowers)-2:
            return -1
        
        garden = [0]* len(flowers) 
        for i, x in enumerate(flowers):
            #x: position, i: day
            garden[x-1] = i+1
 
        #maintain a monotonic increasing queue, dq[0] is the minimum
        dq = collections.deque()
        ans = float('inf')
        for j in range(1, len(flowers)-1):
            while dq and garden[dq[-1]] > garden[j]:
                dq.pop()
            dq.append(j)
            
            #print [garden[x] for x in dq]
            #window is [j-k+1, j], to compare with j-k (left) and j+1(right)
            if dq[0]== j-k :
                dq.popleft()
        
            
            #first valid window is [1,k] to compare with 0 and k+1
            if j>=k:
                if k==0 or garden[dq[0]] > max(garden[j-k], garden[j+1]):
                #condition k==0 here is to deal with corner cases dp is empty when k=0
                    ans = min(ans, max(garden[j+1], garden[j-k]))
                
        return ans if ans < float('inf') else -1

    
#-Method 2-Another mono queue (min queue for this case)

from collections import deque
class MinQueue(deque):
    def __init__(self):
        deque.__init__(self)
        self.mins = deque()

    def append(self, x):
        deque.append(self, x)
        while self.mins and x < self.mins[-1]:
            self.mins.pop()
        self.mins.append(x)

    def popleft(self):
        x = deque.popleft(self)
        if self.mins[0] == x:
            self.mins.popleft()
        return x

    def min(self):
        return self.mins[0]

class Solution(object):
    def kEmptySlots(self, flowers, k):
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        window = MinQueue()
        ans = len(days)

        for i, day in enumerate(days):
            window.append(day)
            if k <= i < len(days) - 1:
                window.popleft()
                if k == 0 or days[i-k] < window.min() > days[i+1]:
                    ans = min(ans, max(days[i-k], days[i+1]))

        return ans if ans <= len(days) else -1
    
    
# -Method 3- Two pointers Sliding window method
class Solution(object):
    def kEmptySlots(self, flowers, k):
        #two pointers sliding window solution
        
        days = [0] * len(flowers)
        for day, position in enumerate(flowers, 1):
            days[position - 1] = day

        ans = float('inf')
        left, right = 0, k+1
        while right < len(days):
            for i in xrange(left + 1, right):
                if days[i] < days[left] or days[i] < days[right]:
                    #instead of left+1 and right+1
                    #use i, i+k+1 as a new window, which makes O(n)
                    left, right = i, i+k+1
                    break 
                    #break the for loop without executing else statement
            else:
                #this else statement is executed only when the for loop ends (not breaks)
                ans = min(ans, max(days[left], days[right]))
                #skip k length, and make a new window staring from right
                left, right = right, right+k+1

        return ans if ans < float('inf') else -1
    
    
 # -Method 4- Brutal Force  TLE O((n-k)*k)   worst case O(n^2) when k =n/2
 class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if k <0  or k > len(flowers)-2:
            return -1
        
        garden = [0]* len(flowers) 
        for i, x in enumerate(flowers):
            #x: position, i: day
            garden[x-1] = i+1
 
        #brutal force (n-k)*k
        ans = float('inf')
        for j in range(k+1, len(flowers)):
            if k>0:
                middle_min = min(garden[j-k:j])
                if middle_min > max(garden[j], garden[j-k-1]):
                    ans = min(ans, max(garden[j], garden[j-k-1]))
            else:
                ans = min(ans, max(garden[j], garden[j-k-1]))
            
                
        return ans if ans < float('inf') else -1
