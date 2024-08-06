class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        rem = numBottles

        while numExchange<=rem:

            temp = rem//numExchange
            rem = rem%numExchange
            res+=temp
            rem += temp
        return res