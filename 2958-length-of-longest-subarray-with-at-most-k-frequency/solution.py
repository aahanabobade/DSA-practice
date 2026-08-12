# Length of Longest Subarray With at Most K Frequency
# Difficulty: Medium
# Runtime: 350 ms
# Memory: 23.4 MB
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

        """
        freq = {}
        left = 0
        ans = 0

        for right in range(len(nums)):
            # Add current element
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # Shrink window if frequency exceeds k
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            # Current window is valid
            ans = max(ans, right - left + 1)

        return ans
