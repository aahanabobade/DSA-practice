// Rearrange Array Elements by Sign
// Difficulty: Medium
// Runtime: 4 ms
// Memory: 75.9 MB
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution {
    public int[] rearrangeArray(int[] nums) {
        // Create two pointers to keep track of positive and negative indices
        int posIndex = 0, negIndex = 1;
        int[] result = new int[nums.length];
        
        // Iterate through the original array
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                // Place positive numbers at even indices
                result[posIndex] = nums[i];
                posIndex += 2;
            } else {
                // Place negative numbers at odd indices
                result[negIndex] = nums[i];
                negIndex += 2;
            }
        }
        
        // Copy result back to nums array to achieve in-place rearrangement
        for (int i = 0; i < nums.length; i++) {
            nums[i] = result[i];
        }
        
        return nums;
    }
}
