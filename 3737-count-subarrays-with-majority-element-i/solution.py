# Count Subarrays With Majority Element I
# Difficulty: Medium
# Runtime: 1231 ms
# Memory: 12.7 MB
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

        n = len(nums)

        arr = [1 if x == target else -1 for x in nums]

        ans = 0

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s > 0:
                    ans += 1

        return ans
