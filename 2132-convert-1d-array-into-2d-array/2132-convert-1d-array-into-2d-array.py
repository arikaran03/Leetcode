class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) == m*n:
            
            array = [[0 for i in range(n)] for i in range(m)]
            i = 0
            for row in range(m):

                for col in range(n):
                    if i>len(original):
                        break
                    array[row][col] = original[i]
                    i+=1
        else : return []

        return array