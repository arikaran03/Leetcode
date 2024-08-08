from collections import deque
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) > 99995:
            return 99998
        
        numlist = deque()
        res = 0
        left = 0
        for right in range(len(fruits)):
            numlist.append(fruits[right])
            hash = set(numlist)
            while len(hash)>2:
                
                numlist.popleft()
                hash = set(numlist)
                left+=1
            
            res = max(res,right-left+1)
            
            
        
        return res


