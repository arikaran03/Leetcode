class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        rem = 0
        Empty = 0
        drink = 0
        while  numExchange <= Empty or numBottles !=0:

            if numExchange > Empty:
                Empty  += numBottles
                drink += numBottles
                numBottles = 0
            elif numExchange <= Empty:
                
                temp = Empty-numExchange
                numExchange += 1
                numBottles +=1
                Empty = temp

        return drink 