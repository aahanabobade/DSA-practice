# Minimum Absolute Distance Between Mirror Pairs
# Difficulty: Medium
# Runtime: 206 ms
# Memory: 41.8 MB
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/


        for j, num in enumerate(nums):
            # Look up num — earlier entries stored reverse(nums[i]) as key
            if num in index_map:
                min_distance = min(min_distance, j - index_map[num])

            # Store reverse(num) → j, overwriting older index (only need the latest)
            reversed_num = int(str(num)[::-1])
            index_map[reversed_num] = j

        min_distance = float('inf')
        index_map = {}
