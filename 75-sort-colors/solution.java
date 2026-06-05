// Sort Colors
// Difficulty: Medium
// Runtime: 0 ms
// Memory: 42.1 MB
// https://leetcode.com/problems/sort-colors/

class Solution {
    public void sortColors(int[] nums) {
        int low = 0;
        int mid = 0;
        int high = nums.length - 1;
        
        // Iterate through the array
        while (mid <= high) {
            if (nums[mid] == 0) {
                // Swap nums[low] and nums[mid] and increment both low and mid
                swap(nums, low, mid);
                low++;
                mid++;
            } else if (nums[mid] == 1) {
                // Just move the mid pointer as 1's should stay in the middle
                mid++;
            } else {
                // Swap nums[mid] and nums[high] and decrement high pointer
                swap(nums, mid, high);
                high--;
            }
        }
    }
    
    // Helper function to swap two elements in the array
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}

