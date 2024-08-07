public class Solution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        int rem = 0;
        int Empty = 0;
        int drink = 0;

        while (numExchange <= Empty || numBottles != 0) {
            if (numExchange > Empty) {
                Empty += numBottles;
                drink += numBottles;
                numBottles = 0;
            } else if (numExchange <= Empty) {
                int temp = Empty - numExchange;
                numExchange++;
                numBottles++;
                Empty = temp;
            }
        }

        return drink;
    }
}