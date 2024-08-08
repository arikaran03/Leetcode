class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def sub(s,p):

            i = 0
            j = 0

            while i<len(s) and j<len(p):
                
                if i in remove or s[i] != p[j]:
                    i+=1
                    continue
                else:
                    i+=1
                    j+=1
            return  j == len(p)

        left = 0
        right = len(removable)-1

        res = 0
        
        
        while left<=right:

            mid = (left+right)//2

            remove = set()
            for x in  range(mid+1):
                remove.add(removable[x])

            if sub(s,p):
                left = mid+1
                res = max(res,mid+1)
            else:
                right = mid-1
        return res
              