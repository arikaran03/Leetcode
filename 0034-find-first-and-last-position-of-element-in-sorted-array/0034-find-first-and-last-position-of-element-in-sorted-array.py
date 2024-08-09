from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]

        def binary(array,mid,left,right,check):
            res = -2
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



        left = 0
        right = len(nums)-1
        one = False
        mid = 0
        while left<=right:

            mid = (left+right)//2

            if nums[mid] == target:
                one = True
                break

            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if not one:
            return [-1,-1]
        else:
            
            leftval = binary(nums,mid,0,mid-1,False)
            rightval = binary(nums,mid,mid+1,len(nums)-1,True)

            if leftval == -2:
                leftval = mid
            if rightval == -2:
                rightval = mid
            return [leftval,rightval]