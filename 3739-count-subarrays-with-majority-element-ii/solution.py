# Count Subarrays With Majority Element II
# Difficulty: Hard
# Runtime: 1032 ms
# Memory: 34.4 MB
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/

            pref.append(cur)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        bit = Fenwick(len(vals))
        ans = 0

        for p in pref:
            r = rank[p]
            ans += bit.query(r - 1)   # previous prefix sums < current
            bit.add(r, 1)

        return ans
