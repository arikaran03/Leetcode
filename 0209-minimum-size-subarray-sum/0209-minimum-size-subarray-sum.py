class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        min_idx = float('inf')
        sum = 0
        for right in range(len(nums)):
            sum += nums[right]
            
            while sum>=target:

                min_idx = min(min_idx, right-left+1)
                sum -= nums[left]
                left+=1
    
        return min_idx if min_idx!= float('inf') else 0