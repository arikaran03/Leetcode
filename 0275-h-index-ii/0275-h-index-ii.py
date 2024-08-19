class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) ==1 and citations[0] == 0:
            return 0
        citations = citations[::-1]
        
        idx = 0
        prev = citations[0]
        check = True

        while idx<len(citations):
            if citations[idx] !=0:
                check = False
            
            if citations[idx] < idx+1:
                
                if check:
                    return 0

                return idx
            elif citations[idx] <= idx+1:
                if check:
                    return 0

                return idx+1
                
            prev = citations[idx]
            idx += 1
            
        return idx