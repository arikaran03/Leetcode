from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        """if not nums:
            return [-1,-1]"""
        
        def binary(array,check,target):
            left = 0
            right = len(nums)-1
            res = -1
            while left<=right:
                mid = (left+right)//2

                if target == array[mid]:
                    res = mid
                    if check == True:
                        left = mid+1
                    else:
                        right = mid-1

                elif array[mid] <= target:
                    left = mid+1
                else:
                    right = mid-1

            
            return res

        leftval = binary(nums,False,target)
        rightval = binary(nums,True,target)

        return [leftval,rightval]
            