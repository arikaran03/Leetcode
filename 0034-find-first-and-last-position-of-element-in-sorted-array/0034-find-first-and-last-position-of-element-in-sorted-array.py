class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(nums,target,search):

            left = 0
            right = len(nums)-1
            idx = -1

            while left<=right:

                mid = (left+right)//2

                if nums[mid] == target:
                    idx = mid

                    if search:
                        
                        right = mid-1
                    else:
                        left = mid+1
                elif nums[mid] > target:
                    
                    right = mid-1
                else:

                    left = mid+1
            return idx
        
        leftval = binary_search(nums,target,True)
        rightval = binary_search(nums,target,False)
        return [leftval,rightval]
