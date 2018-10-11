"""
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
"""

#easily solvable by one-pass sliding window

def summaryRanges(self, nums):
    if len(nums)==0: return []
    if len(nums)==1: return [str(nums[0])]

    l, r = 0, 1
    ans =[ ]
    nums = nums + [float('inf')]
    while r<len(nums):
        if nums[r] == nums[r-1] +1:
            r += 1
        else:
            if l< r-1:
                ans.append(str(nums[l]) +"->"+str(nums[r-1]))
            else:
                ans.append(str(nums[l]))
            l , r = r, r+1
    return ans
