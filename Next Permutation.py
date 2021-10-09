import sys
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if(len(nums)<=1):
            return
        
        maxPrev = nums[-1]
        for i in range(len(nums)-2, -2, -1):
           
            if(i>=0 and nums[i] < maxPrev):
                break
            maxPrev = max(maxPrev, nums[i])
        
        if(i>=0):
            minAfter = sys.maxsize
            minAfterIndex = i+1
           
            temp = nums[i]
            for j in range(len(nums)-1,i,-1):
                if(nums[j] > temp and nums[j] < minAfter):
                    minAfter = nums[j]
                    minAfterIndex = j
            
            
            nums[minAfterIndex] = temp
            nums[i] = minAfter
            
            start, end = i+1, len(nums)-1
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            
        else:
           
            nums.sort()
