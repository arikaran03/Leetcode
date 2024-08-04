class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        newarray = nums

        for i in range(n):
            val = nums[i]
            for j in range(i+1,n):
                val +=nums[j]
                
                newarray.append(val)
        
        newarray.sort()
        print(newarray)
        sumval = sum(newarray[left-1:right])
        print(sum(newarray))
        return sumval%(10**9+7)

        

             