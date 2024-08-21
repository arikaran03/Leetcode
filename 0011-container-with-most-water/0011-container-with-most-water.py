from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_val = 0
        left = 0
        right = len(height)-1

        while left<=right:

            dis = right-left
            min_val = min(height[left],height[right])
            max_val = max(max_val, dis*min_val)
      
            if height[left]<height[right]:
                left+=1
            
            else:
                right-=1
        return max_val