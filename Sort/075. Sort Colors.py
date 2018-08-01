class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n0=n1=n2=-1
        #pointer/counter that points to the end of 0, 1, 2 respectively
        
        for x in nums:
            if x ==0:
                # a ZERO will push all pointers to the right by one
                n2, n1, n0 = n2+1, n1+1, n0+1
                nums[n2] , nums[n1], nums[n0] = 2, 1, 0
             
            elif x==1:
                # a ONE will push n2 and n1 to the right by one
                n2, n1 = n2+1, n1+1  
                nums[n2] , nums[n1] = 2, 1 
             
            elif x==2:
                # a TWO will only affect n2 
                n2 = n2+1
                nums[n2] = 2
                
            print nums
 
    
    
 
   
        
                
            
