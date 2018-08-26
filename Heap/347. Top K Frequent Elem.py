#verbose version for interview
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #O(n)
        cnt = collections.defaultdict(int)
        for x in nums: cnt[x] +=1 
        
        #O(n)
        q = [(-cnt[i],i) for i in cnt]
        
        #O(nlogn)
        heapq.heapify(q)
        
        ans = []
        #O(klogn)
        for i in range(k):
            ans.append(heapq.heappop(q)[1] )
            
        return ans

#heapq.nlargest method
class Solution(object):
    def topKFrequent(self, nums, k):
        """ Given a non-empty array of integers, return the k most frequent elements.
        heapq.nlargest(n, iterable[, key])
        Return a list with the n largest elements from the dataset defined by iterable.
        """
        num_count = collections.Counter(nums)
        return heapq.nlargest(k, num_count, key=lambda x: num_count[x])

#Counter object most_common method
class Solution_2(object):
    def topKFrequent(self, nums, k):
        ''' Use Counter to extract the top k frequent elements
        most_common(k) return a list of tuples,
        where the first item of the tuple is the element,
        and the second item of the tuple is the count
        Thus, the built-in zip function could be used to extract
        the first item from the tuples
        '''
        return zip(*collections.Counter(nums).most_common(k))[0]
