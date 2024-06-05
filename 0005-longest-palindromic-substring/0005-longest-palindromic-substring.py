class Solution:
    def longestPalindrome(self, s: str) -> str:
        b=[]
        maxi=""
        if len(s)==1 or s==s[::-1]:
            return s
        
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                a=s[i:j+1]
                if a==a[::-1]:
                    b.append(a)
        
        
        for i in range(len(b)):
            if len(b[i]) > len(maxi):
                maxi=b[i]
        if maxi=="":
            return s[0]
        return maxi
