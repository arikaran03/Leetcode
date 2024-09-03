class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        sum_val = ""

        for i in s:

            sum_val += str(abs(ord(i) - 96))
        

        i = 1
        new_sum = 0
        while i<=k:

            for j in sum_val:
                new_sum += int(j)

            sum_val = str(new_sum)
            new_sum = 0
            i+=1
        return int(sum_val)

            