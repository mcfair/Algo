#idea is that we know exactly how many colors (0, 1,2) are there. So no need to swap.
#naive way is couting sort, cout the numbers of each color and then generate the sorted array based on count. O(n) two pass
#another way is to find the ending location of 0s, 1s, 2s repcetively, which is equivalent to find out the counts.
#Here is the math:
#a 0 will move all pointers to the right by 1
#a 1 will move n1 and n2 to the right by 1
#a 2 will only move n2 to the right 1
#while finding out the new location, filling the array with corresponding number. O(n) one pass

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
       
    
 #straightforward counting sort   O(n) time  
 class Solution(object):
    def sortColors(self, nums):
        cnt = [0]*3
        for x in nums:  
            cnt[x] +=1
        nums[:] =[0]*cnt[0] + [1]*cnt[1] + [2]*cnt[2]
        
                
            
