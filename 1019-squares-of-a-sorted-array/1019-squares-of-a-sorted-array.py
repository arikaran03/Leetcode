class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums)
        i = len(res)-1
        left = 0
        right = len(nums)-1
        
        while left<=right:

            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left]**2
                left+=1
                i-=1
            else:
                res[i] = nums[right]**2
                i-=1
                right-=1
        return res
            