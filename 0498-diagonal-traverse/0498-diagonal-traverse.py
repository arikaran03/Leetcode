class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        row = len(mat)
        col = len(mat[0])

        list1 = [[] for _ in range(row+col-1)]

        for r in range(row):
            for c in range(col):

                even = (r+c)%2

                if even == 0:

                    list1[r+c].insert(0,mat[r][c])
                else:
                    list1[r+c].append(mat[r][c])

        res = []
        for x in range(len(list1)):
            res.extend(list1[x])
        return res