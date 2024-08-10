//import java.util.*;
class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] array = new int[nums.length];
        int left = 0;
        int right = nums.length - 1;
        int idx = nums.length -1;

        while (left<=right){
            if (Math.abs(nums[left]) > Math.abs(nums[right])){
                array[idx] = nums[left]*nums[left];
                left++;
            }
            else{
                array[idx] = nums[right]*nums[right];
                right--;
            }
            idx--;

        }

        return array;
    }
}