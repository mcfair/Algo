#Mono Queue Algorithm O(n)

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
