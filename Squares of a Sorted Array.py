    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r,k = 0,n-1,n-1           # 2 pointers and k to update the value in result
        result = [0]*n              # for storing the square value
        for _ in range(n):
            if abs(nums[l]) < abs(nums[r]):  # right is greater
                result[k] = nums[r]**2       # update the value to result
                r -= 1                       # reduce the right pointer
            else: 
                result[k]  = nums[l]**2     # update the value to result
                l += 1                     # increment the left pointer
            k -= 1                 # reduce the k index of the result for next cycle
        return result```
