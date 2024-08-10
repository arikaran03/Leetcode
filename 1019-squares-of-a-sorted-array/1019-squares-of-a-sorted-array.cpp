class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> array(nums.size());
        int left = 0;
        int right = nums.size() - 1;
        int idx = nums.size()-1;

        while (left<=right){
            if (abs(nums[left]) > abs(nums[right])){
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
};