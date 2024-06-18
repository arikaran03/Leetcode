class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        

        res = start
        
        for i in range(n-1):
            start+=2
            res ^=start
            
        return res