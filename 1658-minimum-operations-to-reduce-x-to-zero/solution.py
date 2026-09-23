# Minimum Operations to Reduce X to Zero
# Difficulty: Medium
# Runtime: 89 ms
# Memory: 20.7 MB
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

                curr_sum -= nums[left]
                left += 1

            # Found a valid subarray.
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len

