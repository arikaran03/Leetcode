class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) ==1 and citations[0] == 0:
            return 0
        citations = citations[::-1]
        
        idx = 0
        left = 0
        right = len(citations)-1 

        while left<=right:

            idx = (left+right)//2
            
            if citations[idx] == idx+1:
                
                return idx+1
            
            if citations[idx] > idx+1:
                left = idx+1
            else:
                right = idx-1
            
        if citations[idx] < idx+1:

            return idx
        elif citations[idx] <= idx+1:

            return idx+1
        return idx+1