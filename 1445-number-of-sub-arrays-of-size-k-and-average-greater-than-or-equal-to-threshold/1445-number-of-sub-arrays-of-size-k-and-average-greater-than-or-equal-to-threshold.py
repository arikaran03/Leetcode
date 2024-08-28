class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        

        sum_val = sum(arr[0:k])
        left = 0
        count = 0

        if (sum_val//k) >= threshold:
            count+=1
        
        for right in range(k,len(arr)):

            sum_val += arr[right]
            sum_val -= arr[left]
            left+=1

            if (sum_val//k) >= threshold:
                count+=1
            
        return count

        