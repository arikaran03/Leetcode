class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = float('inf')

        for i in strs:
            
            min_len = min(min_len,len(i))
        
        i = 0
        val = strs[0]
        res = ""
        while i<min_len:
            flag = True
            temp = ""
            for j in range(len(strs)):
                if val[i] == strs[j][i]:
                    if val[i] not in temp:
                        temp += val[i]
                    
                else:
                    
                    flag = False
                    i = float('inf')
                    break
            i+=1
            if flag:
                res += temp
        return res