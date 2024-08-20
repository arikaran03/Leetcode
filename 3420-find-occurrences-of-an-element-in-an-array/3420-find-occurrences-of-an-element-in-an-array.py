class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        count = 0
        numlist = []
        res = []
        for i in range(len(nums)):
            if nums[i] == x:
                count +=1
                numlist.append(i)
        
        for j in range(len(queries)):
            
            if count >= queries[j]:
                res.append(numlist[queries[j]-1])
            else:
                res.append(-1)
        return res

        

        