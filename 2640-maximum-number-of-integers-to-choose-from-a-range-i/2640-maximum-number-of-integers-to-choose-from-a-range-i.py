class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = sorted(list(set(banned)))
        # banned.sort()

        ban = 0
        cur_sum = 0
        cnt = 0
        val  = 0
        check = 0
        while cnt < n : 
            cnt += 1
            val += 1
            
            if ban < len(banned) and banned[ban] == val: 
                ban+=1
                continue
            cur_sum += val
            # cnt += 1
            # if cur_sum == maxSum : return cnt
            if cur_sum > maxSum : return check 
            check += 1
            
        return check 