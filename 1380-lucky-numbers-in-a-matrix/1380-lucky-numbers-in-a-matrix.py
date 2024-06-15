class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        for row in range(len(matrix)):
            
            minval = min(matrix[row])
            
            minidx = matrix[row].index(minval)
            one = True
            
            for r in range(len(matrix)):
                
                if minval < matrix[r][minidx]:
                    one = False
                    break
            if one: return [minval]
       