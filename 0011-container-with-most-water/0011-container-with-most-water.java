class Solution {
    public int maxArea(int[] height) {
        int max_val = 0 , min_val=0;
        int left = 0;
        int right = height.length -1;

        while(left<right){
            int dis = right-left;
            if (height[left] < height[right])  min_val = height[left];
            else min_val = height[right];

            int area = dis* min_val;

            if(max_val < area) max_val = area;

            if (height[left] < height[right]) left++;
            else right --;
            
        }
        return max_val;
    }
}