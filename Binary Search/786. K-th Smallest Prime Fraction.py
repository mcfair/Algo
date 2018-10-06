"""
Binary Search + Counting(looped binary search)
"""
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        l, r = 0, 1
        p, q = 0, 1
        n = len(A)
        while l<r:
            mid = (l+r)*0.5
            
            count = 0
            pairIndex = []
            for i in range(n):
                #find elements that satisfies A[i]/A[j] < mid, rewrite it as  A[j] > A[i]/mid
                #we can use bisect_right to find insertion point "j"
                j = bisect.bisect_right(A, A[i]*1.0/mid) 
                #the right half is n-j
                count +=  n - j
                pairIndex.append((i,j))
                
            if count < K:
                l = mid 
            elif count > K:
                r = mid
            else:
                pairs = [(A[i], A[j]) for i, j in pairIndex if j < n]
                return max(pairs, key=lambda x: x[0]*1.0 / x[1])
            
            
#Use heap to make code cleaner.            
def kthSmallestPrimeFraction(self, A, K):
    l, r = 0, 1
    p, q = 0, 1
    n = len(A)
    while l<r:
        mid = (l+r)*0.5
        count = 0
        pairs = []
        for i in range(n):
            j = bisect.bisect_right(A, A[i]*1.0/mid) 
            count +=  n - j
            if j<n: 
                heapq.heappush(pairs, (-1.0*A[i]/A[j],A[i],A[j]))

        if count < K:
            l = mid #since we have a "else" statement, mid+1 doesn't work here
        elif count > K:
            r = mid
        else:
            return heapq.heappop(pairs)[1:]
        
#Found a 75ms solution in Leetcode        
class Solution(object):
    def kthSmallestPrimeFraction(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        
        '''
        Alternative 4: 
        Binary search. 
        Idea is that for a fixed denominator A[j] and numerator A[i], all numbers left of A[i] will produce smaller fraction than A[i]/A[j]. 
        Even though we eventually need a fraction, we start with a decimal, and find our way from the decimal to our fraction. 
        '''
        
        minRatio = 0.0
        maxRatio = 1.0
        while True:
			midRatio = (minRatio + maxRatio) / 2
			i = 0
			k = 0
			maxP, maxQ = 0, 0
			for q in A:
				p = A[i]
				while p < midRatio * q:
					if p * maxQ >= maxP * q:
						maxP = p
						maxQ = q
					i += 1
					p = A[i]
				k += i
			if k > K:
				maxRatio = midRatio
			elif k < K:
				minRatio = midRatio
			else:
				return [maxP, maxQ]


        
        '''
        Alternative 3:
        Min heap. 
        First, we find store 1/prime for all primes greater than 1, as well as the position i,j. 
        [1/5,1/3,1/2]
        Whenever we extract a minimum, we want also i+1, j. (Given that i+1<j)
        
        Submission result: ~6000ms. Beats 30%. 
        '''
        
        minheap = []
        N = len(A)
        for i in xrange(1,N):
            minheap.append((float(1)/A[i],0,i))
        heapq.heapify(minheap)
        
        for _ in xrange(K):
            smallest, i, j = heapq.heappop(minheap)
            if i+1<j:
                heapq.heappush(minheap,(float(A[i+1])/A[j], i+1,j))
        return [A[i],A[j]]
    
        
        '''
        Intuition:
        All numbers in given list are primes. We don't have to worry about common factors. 
        That is, we know for sure every number we created is a valid number. 
        Brute force: Compute all fractions. Sort them and retrive the K-th smallest. 
        Submission result: MLE (memory limit exceeds). 
        
        Alternative: 
        Maintain a heap of K min items.
        We keep a max-heap. When ever we have K+1 items, pop the largest from heap. 
        After we're done, pop the largest. 
        Time complexity: O(N^2*LogK)
        
        Submission result: TLE (time limite exceeds). 
        
        Alternative 2:
        We don't have to actually compute all fractions. 
        We know that 1/5 is smaller than 2/5, which is smaller than 3/5. 
        In fact, we can maintain a K-size heap, but go as the following: 
        
        first/last, first/second-to-last, first/third-to-last......
        second/last, second/second-to-last, .......
        
        Whenever we have the item, we check if the largest fraction is our current fraction. 
        If so, we break from current loop. 
        
        Submission result: ~10000s. Beats 7%. 
        '''
        N = len(A)
        
        fracs = []
    
        #For i = 0,1,2,3,4....
        for i,num in xrange(N):
            #For j = N-1,N-2,N-3.....i+1
            for j in xrange(N-1,i,-1):
                #compute fraction 
                frac = -float(A[i])/A[j]
                heapq.heappush(fracs,(frac, A[i], A[j]))
                if len(fracs)>K:
                    largest = heapq.heappop(fracs)[0]
                    if frac==largest:
                        break 
        frac = heapq.heappop(fracs)
        return [frac[1],frac[2]]
                
        
